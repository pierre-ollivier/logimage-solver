from typing import List, Tuple
import numpy as np


class Board:
    def __init__(self, height: int = None, width: int = None, data: List[List[int]] = None):
        if height is None or width is None:
            if data is None:
                raise ValueError(
                    "Building a board requires providing either its width and its height, or its initial data.")
            else:
                height = len(data)
                width = len(data[0])
        elif data is None:
            data = np.ones(shape=(height, width))
            data *= -1
            data = data.tolist()

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

    def set_square(self, h_coord: int, w_coord: int, value: int) -> None:
        """
        Sets the value of the square of coordinates (`h_coord`, `w_coord`) to `value`. 
        """
        self.data[h_coord][w_coord] = value

    def find_first_empty_square(self) -> Tuple[int, int]:
        data = self.data
        if len(data) == 0:
            raise ValueError(
                "Trying to find an empty square in an empty board, which is nonsense.")
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == -1:
                    return (i, j)
        return (None, None)
