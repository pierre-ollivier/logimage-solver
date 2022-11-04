from typing import List


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
