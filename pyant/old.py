
from tkinter import Tk, Label

WIDTH = 10
HEIGHT = 10


ant_cell = (0, 0)
# Init Tkinter window
root = Tk()
# Matrix of cells
cells = []

def move_ant(root, cells, x, y):
    '''
    Move ant on grid at position (x, y)
    '''
    global ant_cell
    # Current position as old position
    old_pos = ant_cell

    # Clean text and style of old position cell
    old_cell = cells[old_pos[0]][old_pos[1]]
    old_cell['foreground'] = "black"
    old_cell['text'] = ""

    # Get cell at new position and set text
    ant = cells[x][y]
    ant['text'] = 'A'

    # Update current ant position cell variable
    ant_cell = (x, y)



# Init `cells` and Tkinter grid
for h in range(HEIGHT):
    cells.append([])

    for w in range(WIDTH):
        cell = Label(
            root,
            background="white",
            foreground="black",
            text="",
            borderwidth=1,
            width=2,
            relief="sunken",
            padx=0,
            pady=0
        )
        cell.grid(row=w, column=h)

        cells[h].append(cell)


def animate():
    '''
    Recursive animation function
    '''
    global root, cells, ant_cell
    move_ant(root, cells, ant_cell[0] + 1, ant_cell[1] + 1)
    root.after(200, animate)


# Init ant position
move_ant(root, cells, 5, 5)

# Run animation
root.after(200, animate)
# Run Tk
root.mainloop()