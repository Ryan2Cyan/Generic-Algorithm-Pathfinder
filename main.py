import os.path
import random
import pygame
import sys
from Window import windowClass
from Grid import Grid_Class
from FileReader import fileReaderClass
from ChromosomePolulation import Chromosome_Population_Class
from Agent import Agent_Class
from Pathfinder import Pathfinder_Class

"""
Gene Movement Correlation:
00 - Up
01 - Right
10 - Down
11 - Left
"""

def main():

    # Init pygame:
    pygame.init()
    # Init pygame window:
    window = windowClass(400, 400, (0, 0, 0))
    pygame.display.set_caption("Genetic Algorithm Pathfinder")

    # Init file reader and retrieve contents:
    file_reader = fileReaderClass("MazeFilesForLab8/Lab8TerrainFile1.txt")

    # Init GA Pathfinder:
    pathfinder = Pathfinder_Class(
        10, # population size
        16, # chromosome length
        file_reader.contents_of_file.pop(0), # grid width
        file_reader.contents_of_file.pop(0), # grid height
        file_reader.contents_of_file,        # grid values (0, 1, 2, or 3)
        window.screen                        # screen
        )

    # Use Pathfinder to get the fitness values for all chromosomes in this population:
    pathfinder.execute_population([0, 1])


    # Game Loop:
    while True:
        pathfinder.grid.draw_rect_array(window.screen)

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