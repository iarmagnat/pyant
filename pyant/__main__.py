
from board import Board
from insects import Ant, AntiAnt, DoubleAnt


def animate():
    board.play()
    board.window.after(10, animate)

board = Board(161, 71)
board.add_insect(DoubleAnt(board, 0, 0))
# board.add_insect(Ant(board, 81, 20))


# Run animation
board.window.after(100, animate)

board.window.mainloop()