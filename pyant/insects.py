class Insect(object):
    def __init__(self, board, x_pos, y_pos, x_look=0, y_look=1):
        self.board = board
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.x_look = x_look
        self.y_look = y_look

        self.cell = self.board.cells[self.x_pos][self.y_pos]

    def move(self):
        self.cell['text'] = ""
        self.x_pos = (self.x_pos + self.x_look + self.board.x_size) % self.board.x_size
        self.y_pos = (self.y_pos + self.y_look + self.board.y_size) % self.board.y_size

        self.cell = self.board.cells[self.x_pos][self.y_pos]

        self.cell['text'] = "O"


class Ant(Insect):
    def __init__(self, board, x_pos, y_pos, x_look=0, y_look=1):
        super().__init__(board, x_pos, y_pos, x_look, y_look)

        self.cell.arrive(self.look)

    @property
    def look(self):
        if self.x_look == 1 and self.y_look == 0:
            return ">"
        elif self.x_look == -1 and self.y_look == 0:
            return "<"
        elif self.y_look == 1 and self.x_look == 0:
            return "∧"
        elif self.y_look == -1 and self.x_look == 0:
            return "∨"
        else:
            return "BUG"

    def move(self):

        old_cell = self.cell
        if old_cell.status in [0, -1]:
            self.turn(True)
        else:
            self.turn(False)

        self.x_pos = (self.x_pos + self.x_look + self.board.x_size) % self.board.x_size
        self.y_pos = (self.y_pos + self.y_look + self.board.y_size) % self.board.y_size

        self.cell = self.board.cells[self.x_pos][self.y_pos]

        old_cell.depart()
        self.cell.arrive(self.look)

    def turn(self, clockwise):
        if clockwise:
            if self.x_look == 0:
                self.x_look, self.y_look = self.y_look, self.x_look
            else:
                self.x_look, self.y_look = self.y_look, -self.x_look
        else:
            if self.x_look == 0:
                self.x_look, self.y_look = -self.y_look, self.x_look
            else:
                self.x_look, self.y_look = self.y_look, self.x_look


class AntiAnt(Ant):
    def turn(self, clockwise):
        if clockwise:
            if self.x_look == 0:
                self.x_look, self.y_look = -self.y_look, self.x_look
            else:
                self.x_look, self.y_look = self.y_look, self.x_look
        else:
            if self.x_look == 0:
                self.x_look, self.y_look = self.y_look, self.x_look
            else:
                self.x_look, self.y_look = self.y_look, -self.x_look


class DoubleAnt(Ant):
    def __init__(self, board, x_pos, y_pos, x_look=0, y_look=1):
        super().__init__(board, x_pos, y_pos, x_look, y_look)
        self.x_look = self.x_look * 2
        self.y_look = self.y_look * 2
