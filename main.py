import os.path
import random
import pygame
import sys
from Window import windowClass
from Grid import Grid_Class
from FileReader import fileReaderClass
from ChromosomePolulation import Chromosome_Population_Class
from Agent import Agent_Class

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

    # Init Grid class:
    grid = Grid_Class(
        file_reader.contents_of_file.pop(0),
        file_reader.contents_of_file.pop(0),
        file_reader.contents_of_file,
        window.screen)


    # Init Chromosome population:
    population = Chromosome_Population_Class(4, 10)
    print(population.chromosomes)

    # Init Agent and set current pos.
    agent = Agent_Class()
    agent.current_pos = grid.start_pos

    # # Pathfinder for one chromosome:
    print("Current Pos :", agent.current_pos)
    for gene in population.chromosomes[0]:
        CURRENT_MOVE = population.gene_to_move(gene)  # Generate next move array
        print("Current Gene: ", gene)
        print("Current Move:", CURRENT_MOVE)

        if agent.is_out_of_bounds(CURRENT_MOVE, grid.width, grid.height) == True:
            print("Out of Bounds.")
            continue
        if agent.is_hitting_obstacle(CURRENT_MOVE, grid.value_array) == True:
            print("Hit Obstacle.")
            continue
        else:
            agent.current_pos[0] = agent.current_pos[0] + CURRENT_MOVE[0]
            agent.current_pos[1] = agent.current_pos[1] + CURRENT_MOVE[1]
            if grid.path_array[agent.current_pos[0]][agent.current_pos[1]] != 2 and grid.path_array[agent.current_pos[0]][agent.current_pos[1]] != 3:
                grid.path_array[agent.current_pos[0]][agent.current_pos[1]] = 4
            print("Moved to: ", agent.current_pos)

    # Game Loop:
    while True:
        grid.draw_rect_array(window.screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main()