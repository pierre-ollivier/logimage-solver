from board import Board
from typing import List, Tuple
from utils import check_dim, get_following_values
from copy import deepcopy
from exceptions import *


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
            FIRST_VALUE = 1
            SECOND_VALUE = 0
            if sum(self.left_constraints[h]) + sum(self.top_constraints[w]) < (self.height + self.width)/2:
                # The missing value is more likely to be 0 than 1
                (FIRST_VALUE, SECOND_VALUE) = (0, 1)
            # We first try to fill the square
            board_with_fill_1 = deepcopy(board)
            board_with_fill_1.set_square(h, w, FIRST_VALUE)
            try:
                self.surely_fill_empty_squares(board_with_fill_1)
                is_f, sol = self.is_fillable(board_with_fill_1)
                if is_f:
                    return (True, sol)
                else:
                    # So now we try to put a blank square
                    board_with_fill_0 = deepcopy(board)
                    board_with_fill_0.set_square(h, w, SECOND_VALUE)
                    self.surely_fill_empty_squares(board_with_fill_0)
                    is_f, sol = self.is_fillable(board_with_fill_0)
                    if is_f:
                        return True, sol
                    else:
                        return (False, None)
            except NoSolutionError:
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
        # When the first square of a row is filled, fill the next squares according to the constraint
        for i, left_constraint in enumerate(self.left_constraints):
            constraint = left_constraint[0]
            if board.data[i][0] == 1 or constraint == self.width:
                for j in range(constraint):
                    board.set_square(i, j, 1)
                if constraint < self.width:
                    board.set_square(i, constraint, 0)

        # When the first square of a column is filled, fill the next squares according to the constraint
        for j, top_constraint in enumerate(self.top_constraints):
            constraint = top_constraint[0]
            if board.data[0][j] == 1 or constraint == self.height:
                for i in range(constraint):
                    board.set_square(i, j, 1)
                if constraint < self.height:
                    board.set_square(constraint, j, 0)

        # When the maximum count of filled squares is reached in a row, fill the next squares with 0
        for i, left_constraint in enumerate(self.left_constraints):
            sum_constraints = sum(left_constraint)
            for j in range(self.width):
                if sum_constraints <= 0:
                    board.set_square(i, j, 0)
                if board.data[i][j] == 1:
                    sum_constraints -= 1

        # When the maximum count of filled squares is reached in a column, fill the next squares with 0
        for j, top_constraint in enumerate(self.top_constraints):
            sum_constraints = sum(top_constraint)
            for i in range(self.height):
                if sum_constraints <= 0:
                    board.set_square(i, j, 0)
                if board.data[i][j] == 1:
                    sum_constraints -= 1

        # Fill rows and columns where a constraint is partially satisfied

        for i, left_constraint in enumerate(self.left_constraints):
            for j in range(self.width):
                if board.data[i][j] == -1:
                    should_be_continued, n = get_following_values(
                        left_constraint, board.data[i], index=j)
                    if should_be_continued:
                        for k in range(n):
                            if j + k < self.width:
                                board.set_square(i, j + k, 1)
                    else:
                        board.set_square(i, j, 0)
                    break

        for j, top_constraint in enumerate(self.top_constraints):
            for i in range(self.height):
                if board.data[i][j] == -1:
                    should_be_continued, n = get_following_values(
                        top_constraint, [board.data[k][j] for k in range(self.height)], index=j)
                    if should_be_continued:
                        for k in range(n):
                            if i + k < self.height:
                                board.set_square(i + k, j, 1)
                    else:
                        board.set_square(i, j, 0)
                    break

        # When the maximum count of empty squares is reached in a row, fill the next square with 1
        for i, left_constraint in enumerate(self.left_constraints):
            sum_constraints = sum(left_constraint)
            min_space_taken = sum_constraints + len(left_constraint) - 1
            for j in range(self.width):
                if board.data[i][j] == 1:
                    return  # nothing can be concluded
                if self.width - j <= min_space_taken:
                    board.set_square(i, j, 1)
                    self.surely_fill_empty_squares(board)  # recursive call

        # When the maximum count of empty squares is reached in a column, fill the next square with 1
        for j, top_constraint in enumerate(self.top_constraints):
            sum_constraints = sum(top_constraint)
            min_space_taken = sum_constraints + len(top_constraint) - 1
            for i in range(self.height):
                if board.data[i][j] == 1:
                    return  # nothing can be concluded
                if self.height - i <= min_space_taken:
                    board.set_square(i, j, 1)
                    self.surely_fill_empty_squares(board)  # recursive call

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
