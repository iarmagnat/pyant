from tkinter import Tk, Label
from insects import Insect


class Board(object):

    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size

        self.window = Tk()
        self.cells = []
        self.insects = []
        for x in range(self.x_size):
            self.cells.append([])
            for y in range(self.y_size):
                self.cells[x].append(Cell(self, x, y))

    def add_insect(self, insect: Insect):
        self.insects.append(insect)

    def play(self):
        for insect in self.insects:
            insect.move()


class Cell(Label):

    def __init__(self, board, x, y):
        super().__init__(
            board.window,
            background="white",
            foreground="black",
            text="",
            borderwidth=1,
            width=2,
            font=("Times", 4, "bold"),
            relief="sunken",
            padx=0,
            pady=0
        )
        self.grid(row=(board.y_size - y), column=x)

        """
        status table:
        -1: white
        0: white, occupied
        
        1: black
        2: black, occupied
        """
        self.status = -1

    def depart(self, change=True):
        self['text'] = ""
        if change:
            if self.status in [0, -1]:
                self.status = 1
            else:
                self.status = -1
        else:
            if self.status in [0, -1]:
                self.status = -1
            else:
                self.status = 1
        self.update()

    def arrive(self, text):
        self['text'] = text
        self.status += 1
        self.update()

    def update(self):
        if self.status in [0, -1]:
            self['background'] = "white"
            self['foreground'] = "black"
        else:
            self['background'] = "black"
            self['foreground'] = "white"
