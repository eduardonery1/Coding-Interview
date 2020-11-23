class Node:
    def __init__(self, value, left = None, right = None, children=[]):
        self.value = value
        self.right = right
        self.left = left
        self.marked = False
        self.children = children


class Tree:
    pass