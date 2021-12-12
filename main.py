import os.path
import random
import pygame
import sys
from Window import windowClass
from FileReader import fileReaderClass
from Pathfinder import Pathfinder_Class

"""
Gene Movement Correlation:
00 - Up
01 - Right
10 - Down
11 - Left
"""

# sets text on the screen to be printed
def set_text(message, x_coord, y_coord, fontSize): #Function to set text
    font = pygame.font.Font('Font\JetBrainsMono-Light.ttf', fontSize)
    #(0, 0, 0) is black, to make black text
    text = font.render(message, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.right = x_coord
    textRect.top = y_coord
    return (text, textRect)

def main():

    # Init pygame:
    pygame.init()
    # Init pygame window:
    window = windowClass(400, 400, (0, 0, 0))
    pygame.display.set_caption("A2: Genetic Algorithm Pathfinder")

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
    pathfinder.execute_population()

    numb_array = []


    # Game Loop:
    while True:
        # print grid:
        pathfinder.grid.draw_rect_array(window.screen)

        # print 'path taken' text:
        # want to display: i) Population ii) Fitness iii) Path
        populationText = set_text("Population:", 390, 335, 15)
        window.screen.blit(populationText[0], populationText[1])
        chromosomeText = set_text("Chromosome:", 390, 355, 15)
        window.screen.blit(chromosomeText[0], chromosomeText[1])
        pathText = set_text("Path: [0,1]", 390, 375, 15)
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