import os.path
import pygame
import sys

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
            GRID_VALUES = []
            i = 0

            # create 2-D grid
            for row in range(HEIGHT):
                GRID_VALUES.append([])
                for column in range(WIDTH):
                    GRID_VALUES[row].append(0)
                    GRID_VALUES[row][column] = FILE_DATA_ARRAY[i]
                    i = i + 1
            return GRID_VALUES

    # Renders grid to screen:
    def gen_rect_array(self, WIDTH, HEIGHT, SCREEN, VALUES):
        blockSize = 40  # Set the size of the grid block

        rect_array = []
        for x in range(0, HEIGHT * blockSize, blockSize):
            for y in range(0, WIDTH * blockSize, blockSize):
                rect = pygame.Rect(y, x, blockSize, blockSize)
                rect_array.append(rect)

        # 2-D array of Grid Squares
        rect_array = self.sort_grid_array(WIDTH, HEIGHT, rect_array)

        return rect_array

    # Render grid the AI just moved to:
    def draw_rect_array(self, screen):
        for row in range(self.height):
            for column in range(self.width):
                # Grid Fill:
                pygame.draw.rect(screen, self.grid_color(self.value_array[row][column]), self.rect_array[row][column],0)
                # Grid Lines:
                pygame.draw.rect(screen, (10, 30, 200), self.rect_array[row][column], 1)

    # Switch for Grid Square Color:
    def grid_color(self, grid_value):
        if grid_value == 0: # Empty Space
            return (255, 255, 255)
        elif grid_value == 1: # Obstacle
            return (0, 0, 0)
        elif grid_value == 2: # Start
            return (10, 200, 30)
        elif grid_value == 3: # End
            return (10, 40, 200)
        elif grid_value == 4: # Path
            return (200, 150, 150)

    # Find the agent's starting point:
    def find_start_point(self, GRID_ARRAY, HEIGHT, WIDTH):
        starting_pos = []
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if GRID_ARRAY[y][x] == 2:
                    starting_pos.append(y)
                    starting_pos.append(x)
        return starting_pos

    # Find the agent's finish point:
    def find_finish_point(self, GRID_ARRAY, HEIGHT, WIDTH):
        finishing_pos = []
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if GRID_ARRAY[y][x] == 3:
                    finishing_pos.append(y)
                    finishing_pos.append(x)
        return finishing_pos
