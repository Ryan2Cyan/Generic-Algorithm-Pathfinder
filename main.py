# main.py
# Compiler: Python 3.10

import pygame
import sys
from Window import windowClass
from FileReader import fileReaderClass
from Pathfinder import Pathfinder_Class
from AStarPathfinder import A_Star_Pathfinder_Class
from Utility import Grid_Color
import timeit

"""
Gene Movement Correlation:
00 - Up
01 - Right
10 - Down
11 - Left
"""

# sets text on the screen to be printed - probably move to utility:
def set_text(message, x_coord, y_coord, fontSize): #Function to set text
    font = pygame.font.Font('Font\JetBrainsMono-Light.ttf', fontSize)
    #(0, 0, 0) is black, to make black text
    text = font.render(message, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.right = x_coord
    textRect.top = y_coord
    return (text, textRect)

def main():

<<<<<<< HEAD
    # Set other parameters here:
    WINDOW_WIDTH = 400                                          # Grid Width
    WINDOW_HEIGHT = 400                                         # Grid Height
    WINDOW_COLOR = Grid_Color.BLACK.value                       # Window Background Color
    TITLE = "A2: Genetic Algorithm Pathfinder"                  # Title
    GRID_FILE_PATH = "MazeFilesForLab8/Lab8TerrainFile1.txt"    # Grid File
=======
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 400
    WINDOW_COLOR = Grid_Color.BLACK.value
    TITLE = "A2: Genetic Algorithm Pathfinder"
    GRID_FILE_PATH = "MazeFilesForLab8/Lab8TerrainFile1.txt"
>>>>>>> 3eeca32859c952e96ddaf59f5c3e04e345082acc

    # Init pygame:
    pygame.init()

    # Init pygame window:
    window = windowClass(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_COLOR)
    pygame.display.set_caption(TITLE)

    # Init file reader and retrieve contents:
    file_reader = fileReaderClass(GRID_FILE_PATH)

    # Init GA Pathfinder:
    POPULATION_SIZE = 50
    CHROMOSOME_LENGTH = 40

    pathfinder = Pathfinder_Class(
        POPULATION_SIZE, # population size
        CHROMOSOME_LENGTH, # chromosome length
        file_reader.contents_of_file.pop(0), # grid width
        file_reader.contents_of_file.pop(0), # grid height
        file_reader.contents_of_file,        # grid values (0, 1, 2, or 3)
        window.screen                        # screen
        )

    # Use Pathfinder to get the fitness values for all chromosomes in this population:
    path_chromosome = pathfinder.execute_population()

    execution_time = timeit.timeit(lambda: pathfinder.execute_population(), number=1)
<<<<<<< HEAD
    print(f"Execution Time:", float("{0:.3f}".format(execution_time * 1000)), "ms")
    print("Final Path:", path_chromosome)
=======
    print(f"Execution Time:" ,float("{0:.3f}".format(execution_time * 1000)), "ms")
>>>>>>> 3eeca32859c952e96ddaf59f5c3e04e345082acc


    print("Final Path: ", path)

    # Display Loop:
    while True:
        # print grid:
        pathfinder.grid.draw_rect_array(window.screen)

        # display text:
        # want to display: i) Population ii) Chromosome Numb iii) Path
        population_message = "Generation: " + str(pathfinder.current_gen)
        population_text = set_text(population_message, 390, 315, 15)
        window.screen.blit(population_text[0], population_text[1])

        chromosome_message = "Chromosome Numb: " + str(pathfinder.current_chromosome)
        chromosome_text = set_text(chromosome_message, 390, 335, 15)
        window.screen.blit(chromosome_text[0], chromosome_text[1])

        pathText = set_text(str(path_chromosome), 390, 375, 14)
        window.screen.blit(pathText[0], pathText[1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                del pathfinder
                del file_reader
                del window
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main()