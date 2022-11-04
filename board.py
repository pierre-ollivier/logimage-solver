from typing import List
import numpy as np


class Board:
    def __init__(self, height: int = None, width: int = None, data: np.ndarray = None):
        if height is None or data is None:
            if data is None:
                raise ValueError("Building a board requires providing either its width andits height, or its initial data.")
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
                    to_print += "X"
                else:
                    to_print += " "
            line_to_print += "|"

            total_to_print += "\n" + line_to_print
        total_to_print += "\n" + " " + "-" * (2*self.width + 1)

        print(total_to_print)