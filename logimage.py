from typing import List


class Logimage:

    def __init__(self, leftLists: List[List[int]] = None, topLists: List[List[int]] = None):
        if leftLists is None:
            leftLists = []
        if topLists is None:
            topLists = []
        self.height = len(leftLists)
        self.width = len(topLists)
