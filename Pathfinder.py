import os.path
import pygame
import sys
import random
import numpy
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
            self.population.fitness_array.append(self.calculate_fitness(self.agent.current_pos, self.grid.finish_pos))

            # Select parent chromosomes:
            parents = self.roulette_wheel_select(self.population.fitness_array)
            print(parents)


    # Calculates the fitness of a single chromosome:
    def calculate_fitness(self, final_position, end_goal):
        y_offset = abs(end_goal[0] - final_position[0])
        x_offset = abs(end_goal[1] - final_position[1])
        return round((1 / (x_offset + y_offset + 1)),2)

    # Roulette wheel chromosome selector - returns an array of indexes for chosen parent chromosomes:
    def roulette_wheel_select(self, fitness_array):

        # Calculate total fitness:
        total_fitness = round(sum(fitness_array),2)

        # Calculate probability for each fitness:
        fitness_probabilities = []
        for fitness_value in fitness_array:
            fitness_probabilities.append(round((fitness_value / total_fitness) * 100,2))

        # Make array of indexes to reference what chromosomes will be picked:
        chromosome_indexes = [x for x in range(len(fitness_array))]

        # Choose parent chromosomes:
        parents_indexes = (numpy.random.choice(chromosome_indexes, 20, fitness_probabilities))

        # Return the parent chromosomes
        chosen_chromosomes = []
        for index in parents_indexes:
            chosen_chromosomes.append(self.population.chromosomes[index])

        return chosen_chromosomes









