from logimage import Logimage
from board import Board
from utils import check_dim
import numpy as np


def test8checkdim():
    assert check_dim(constraints=[1, 2], board_extract=[
        1, 0, 0, 1, 1, 0, 0])
    assert check_dim(constraints=[1, 2], board_extract=[
        0, 1, 0, 0, 1, 1, 0, 0])


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

    assert log.is_solution(board2)
    assert not(log.is_solution(board))


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

    assert log.is_solution(board)


def run():
    test0()
    test1()
    print("All tests were run, no error was encountered!")
