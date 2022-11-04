import board
import logimage
import numpy as np

b = board.Board(height=8, width=6)
b.draw()

c = board.Board(data=np.array([
                              [0, 1, 1, 1, 0],
                              [1, 1, 1, 0, 0],
                              [1, 1, 1, 1, 1],
                              [0, 0, 0, 0, 1]
                              ]))
c.draw()
