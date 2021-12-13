import pygame
from Window import windowClass
from FileReader import fileReaderClass
from Pathfinder import Pathfinder_Class
from Utility import Grid_Color

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

    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 400
    WINDOW_COLOR = Grid_Color.BLACK.value
    TITLE = "A2: Genetic Algorithm Pathfinder"

    # Init pygame:
    pygame.init()

    # Init pygame window:
    window = windowClass(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_COLOR)
    pygame.display.set_caption(TITLE)

    # Init file reader and retrieve contents:
    file_reader = fileReaderClass("MazeFilesForLab8/Lab8TerrainFile1.txt")

    # Init GA Pathfinder:
    POPULATION_SIZE = 10
    CHROMOSOME_LENGTH = 16

    pathfinder = Pathfinder_Class(
        POPULATION_SIZE, # population size
        CHROMOSOME_LENGTH, # chromosome length
        file_reader.contents_of_file.pop(0), # grid width
        file_reader.contents_of_file.pop(0), # grid height
        file_reader.contents_of_file,        # grid values (0, 1, 2, or 3)
        window.screen                        # screen
        )

    # Use Pathfinder to get the fitness values for all chromosomes in this population:
    pathfinder.execute_population()

    # Game Loop:
    while True:
        # print grid:
        pathfinder.grid.draw_rect_array(window.screen)

        # display text:
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