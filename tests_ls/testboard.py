from logimage import Logimage
from board import Board
import numpy as np


def test0():
    log = Logimage(
        top_constraints=[[1, 1, 2]],
        left_constraints=[[1], [], [1], [], [1], [1], []]
    )

    board = Board(data=([
                        [1, 0, 1, 0, 1, 1, 0]
                        ]))

    board2 = Board(data=([
        [1], [0], [1], [0], [1], [1], [0]
    ]))

    board.draw()
    board2.draw()

    assert board2.is_solution(log)
    assert not(board.is_solution(log))


def test1():
    log = Logimage(
        left_constraints=[[1, 1, 1],
                          [3, 2],
                          [4]
                          ],
        top_constraints=[[2], [2], [3], [1], [3], [1]]
    )

    board = Board(data=([
                        [1, 0, 1, 0, 1, 0],
                        [1, 1, 1, 0, 1, 1],
                        [0, 1, 1, 1, 1, 0]
                        ]))

    board.draw()

    assert board.is_solution(log)


def run():
    test0()
    test1()
    print("All tests were run, no error was encountered!")
