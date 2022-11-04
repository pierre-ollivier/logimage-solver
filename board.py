from typing import List
import numpy as np
from logimage import Logimage


class Board:
    def __init__(self, height: int = None, width: int = None, data: np.ndarray = None):
        if height is None or width is None:
            if data is None:
                raise ValueError(
                    "Building a board requires providing either its width and its height, or its initial data.")
            else:
                (height, width) = data.shape
        elif data is None:
            data = np.ones(shape=(height, width))
            data *= -1

        self.height = height
        self.width = width
        self.data = data

    def draw(self):
        total_to_print = " " + "-" * (2*self.width + 1)
        for row in range(self.height):
            line_to_print = "| "
            for column in range(self.width):
                if self.data[row][column] == 1:
                    line_to_print += "X "
                else:
                    line_to_print += "  "
            line_to_print += "|"

            total_to_print += "\n" + line_to_print
        total_to_print += "\n" + " " + "-" * (2*self.width + 1)

        print(total_to_print)

    def is_solution(self, log: Logimage -> bool):
        """
        Checks whether the `Board` instance is a solution of the logimage `log`.
        """
        if self.height != log.height or self.width != log.width:
            return False

        def check_dim(constraints: List[int], board_extract: List[int]):
            """
            Checks whether a line or column extracted from a `Board` respects the constraints.
            Args:
            `constraints`: the constraints, for example [1, 3, 2].
            `board_extract`: the extract from the board, where 1 corresponds to a full square, 0 to an empty square, and -1 to a square
            that is undetermined.
            Returns `True` if `board_extract_ contains only 0s and 1s and the constraints are satisfied.
            """
            if constraints == []:
                # with no constraints, all the squares should be blank
                return board_extract == len(board_extract) * [0]
            elif board_extract[0] == 0:
                # recursive call
                return check_dim(constraints, board_extract[1:])
            elif board_extract[0] == 1:
                condition = True
                consecutive_1s = 1
                while condition:
                    if consecutive_1s == len(board_extract):
                        condition = False  # the whole extract is filled with 1s
                    elif board_extract[consecutive_1s] == 1:
                        consecutive_1s += 1
                    else:
                        condition = False  # we reached a 0 (or a -1)
                if constraints[0] == consecutive_1s:
                    # recursive call
                    return check_dim(constraints[1:], board_extract[consecutive_1s:])
                else:  # wrong count of full squares
                    return False
            elif board_extract[0] == -1:
                return False  # corresponds to an undetermined case
            else:
                raise ValueError("A board should only contain the values -1, 0 or 1. But we found the value "
                                 + str(board_extract[0]))
