from board import Board
from logimage import Logimage
from typing import List, Tuple
from copy import deepcopy

def is_fillable(board: Board, log: Logimage) -> Tuple[bool, Board]:
    (h, w) = board.find_first_empty_square()
    if h is None:
        return board.is_solution(log)
    else:
        # We first try to fill the square
        board_with_fill_1 = deepcopy(board)
        board_with_fill_1.set_square(h, w, 1)
        board_with_fill_1.surely_fill_empty_squares()
        is_f, _ = is_fillable(board_with_fill_1)
        if is_f:
            return True, board_with_fill_1
        else:
            # So now we try to put a blank square
            board_with_fill_0 = deepcopy(board)
            board_with_fill_0.set_square(h, w, 0)
            board_with_fill_0.surely_fill_empty_squares()
            is_f, _ = is_fillable(board_with_fill_1)
            if is_f:
                return True, board_with_fill_0
            else:
                return False, None
