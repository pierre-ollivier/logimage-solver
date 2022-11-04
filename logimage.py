from board import Board
from typing import List, Tuple
from utils import check_dim
from copy import deepcopy


class Logimage:

    def __init__(self, left_constraints: List[List[int]] = None, top_constraints: List[List[int]] = None):
        if left_constraints is None:
            left_constraints = []
        if top_constraints is None:
            top_constraints = []
        self.height = len(left_constraints)
        self.width = len(top_constraints)
        self.left_constraints = left_constraints
        self.top_constraints = top_constraints

    def is_fillable(self, board: Board) -> Tuple[bool, Board]:
        (h, w) = board.find_first_empty_square()
        if h is None:
            if self.is_solution(board):
                return (True, board)
            else:
                return (False, None)
        else:
            # We first try to fill the square
            board_with_fill_1 = deepcopy(board)
            board_with_fill_1.set_square(h, w, 1)
            self.surely_fill_empty_squares(board_with_fill_1)
            is_f, sol = self.is_fillable(board_with_fill_1)
            if is_f:
                return (True, sol)
            else:
                # So now we try to put a blank square
                board_with_fill_0 = deepcopy(board)
                board_with_fill_0.set_square(h, w, 0)
                self.surely_fill_empty_squares(board_with_fill_0)
                is_f, sol = self.is_fillable(board_with_fill_0)
                if is_f:
                    return True, sol
                else:
                    return (False, None)

    def solve(self) -> Board:
        empty_board = Board(height=self.height, width=self.width)
        is_f, sol = self.is_fillable(empty_board)
        if is_f:
            return sol
        else:
            raise ValueError(
                "Tried (and failed) to solve a logimage with no solution.")

    def surely_fill_empty_squares(self, board: Board) -> None:
        pass

    def is_solution(self, board: Board) -> bool:
        """
        Checks whether the `Board` instance is a solution of the logimage `log`.
        """
        if self.height != board.height or self.width != board.width:
            return False

        for i, constraint in enumerate(self.left_constraints):
            if not(check_dim(constraint, board.data[i])):
                return False
        for i, constraint in enumerate(self.top_constraints):
            if not(check_dim(constraint, [board.data[k][i] for k in range(len(board.data))])):
                return False
        return True
