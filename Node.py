# Node.py
# Compiler: Python 3.10


class Node_Class:

    # Constructor - Note: the param 'FILE_CONTENTS' must not include the first 2 digits of the grid array (w and h):
    def __init__(self, parent = None, position = None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0


    def __eq__(self, other):
        return self.position == other.position