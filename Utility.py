# Utility.py
# Compiler: Python 3.10

from enum import Enum

class Grid_Color(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (10, 200, 30)
    BLUE = (10, 40, 200)
    PINK = (200, 150, 150)

class Grid_Space(Enum):
    EMPTY = 0
    OBSTACLE = 1
    START = 2
    END = 3
    PATH = 4