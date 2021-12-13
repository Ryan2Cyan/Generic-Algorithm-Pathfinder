import pygame
from Utility import Grid_Color
from Utility import Grid_Space

class Grid_Class:

    # Constructor:
    def __init__(self, width, height, file_contents, screen):
        self.width = width
        self.height = height
        self.value_array = self.sort_grid_array(width, height, file_contents)
        self.path_array = self.value_array
        self.start_pos = self.find_start_point(self.value_array, height, width)
        self.finish_pos = self.find_finish_point(self.value_array, height, width)
        self.rect_array = self.gen_rect_array(width, height, screen, self.value_array)

    # Sorts Grid Values into a 2-D Array
    def sort_grid_array(self, WIDTH, HEIGHT, FILE_DATA_ARRAY):
            grid_values = []
            i = 0

            # create 2-D grid
            for row in range(HEIGHT):
                grid_values.append([])
                for column in range(WIDTH):
                    grid_values[row].append(0)
                    grid_values[row][column] = FILE_DATA_ARRAY[i]
                    i = i + 1
            return grid_values

    # Renders grid to screen:
    def gen_rect_array(self, WIDTH, HEIGHT, SCREEN, VALUES):
        RECT_SIZE = 40  # Set the size of the grid block

        rect_array = []
        for x in range(0, HEIGHT * RECT_SIZE, RECT_SIZE):
            for y in range(0, WIDTH * RECT_SIZE, RECT_SIZE):
                rect = pygame.Rect(y, x, RECT_SIZE, RECT_SIZE)
                rect_array.append(rect)

        # 2-D array of Grid Squares
        rect_array = self.sort_grid_array(WIDTH, HEIGHT, rect_array)

        return rect_array

    # Render grid the AI just moved to:
    def draw_rect_array(self, SCREEN):
        for row in range(self.height):
            for column in range(self.width):
                # Grid Fill:
                pygame.draw.rect(SCREEN, self.grid_color(self.value_array[row][column]), self.rect_array[row][column],0)
                # Grid Lines:
                pygame.draw.rect(SCREEN, (10, 30, 200), self.rect_array[row][column], 1)

    # Switch for Grid Square Color:
    def grid_color(self, GRID_VALUE):
        match GRID_VALUE:
            case Grid_Space.EMPTY.value:
                return Grid_Color.WHITE.value
            case Grid_Space.OBSTACLE.value:
                return Grid_Color.BLACK.value
            case Grid_Space.START.value:
                return Grid_Color.GREEN.value
            case Grid_Space.END.value:
                return Grid_Color.BLUE.value
            case Grid_Space.PATH.value:
                return Grid_Color.PINK.value

    # Find the agent's starting point:
    def find_start_point(self, GRID_ARRAY, HEIGHT, WIDTH):
        starting_pos = []
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if GRID_ARRAY[y][x] == Grid_Space.START.value:
                    starting_pos.append(y)
                    starting_pos.append(x)
        return starting_pos

    # Find the agent's finish point:
    def find_finish_point(self, GRID_ARRAY, HEIGHT, WIDTH):
        finishing_pos = []
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if GRID_ARRAY[y][x] == Grid_Space.END.value:
                    finishing_pos.append(y)
                    finishing_pos.append(x)
        return finishing_pos
