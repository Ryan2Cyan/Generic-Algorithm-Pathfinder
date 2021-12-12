import os.path
import pygame
import sys
import random
from Window import windowClass
from Grid import Grid_Class
from FileReader import fileReaderClass
from ChromosomePolulation import Chromosome_Population_Class
from Agent import Agent_Class

class Pathfinder_Class:

    # Constructor - Note: the param 'file_contents' must not include the first 2 digits of the grid array (w and h):
    def __init__(self, population_size, chromosome_length, grid_width, grid_height, file_contents,
                 screen):
        self.population = Chromosome_Population_Class(population_size, chromosome_length)
        self.grid = Grid_Class(grid_width, grid_height, file_contents, screen)
        print(self.grid.start_pos)
        self.agent = Agent_Class(self.grid.start_pos)

    # This function executes the moves of all chromosomes in a population
    # and returns an array of 'fitness' for each chromosome:
    def execute_population(self):
        for chromosome in self.population.chromosomes:
            print(chromosome, "\n")

            # Reset agent to start pos:
            self.agent.current_pos[0] = self.grid.start_pos[0]
            self.agent.current_pos[1] = self.grid.start_pos[1]

            # Execute the genes (moves) in single chromosome, and see what path it takes:
            for gene in chromosome:
                CURRENT_MOVE = self.population.gene_to_move(gene) # Generate next move as array
                print("Current Pos: ", self.agent.current_pos)
                print("Current Move: ", CURRENT_MOVE)

                # Check for out of bounds or obstacle:
                if self.agent.is_out_of_bounds(CURRENT_MOVE, self.grid.width, self.grid.height) == True:
                    print("Out of Bounds. ~\n")
                    continue
                if self.agent.is_hitting_obstacle(CURRENT_MOVE, self.grid.value_array) == True:
                    print("Hit Obstacle. ~\n")
                    continue

                # Apply move change to agent:
                else:
                    self.agent.current_pos[0] = self.agent.current_pos[0] + CURRENT_MOVE[0]
                    self.agent.current_pos[1] = self.agent.current_pos[1] + CURRENT_MOVE[1]
                    print("Moved to: ", self.agent.current_pos, "~\n")

                # Check if agent has reached the end point:
                if self.agent.current_pos == self.grid.finish_pos:
                    print("Reached End ~\n")
                    break
            # Calculate Fitness of chromosome:



