from typing import List


class Logimage:

    def __init__(self, leftConstraints: List[List[int]] = None, topConstraints: List[List[int]] = None):
        if leftConstraints is None:
            leftConstraints = []
        if topConstraints is None:
            topConstraints = []
        self.height = len(leftConstraints)
        self.width = len(topConstraints)
