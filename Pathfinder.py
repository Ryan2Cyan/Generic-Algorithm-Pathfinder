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
        i = 0
        fitness_array = []
        for chromosome in self.population.chromosomes:
            print("chromosome index: ", i, "###############")

            # Reset agent to start pos:
            self.agent.current_pos[0] = self.grid.start_pos[0]
            self.agent.current_pos[1] = self.grid.start_pos[1]

            # Execute all chromosome moves and return final pos of the agent:
            final_pos = self.execute_chromosome_moves(chromosome)
            print("Final Pos of Agent: ", final_pos)

            # Calc this chromosome's fitness:
            fitness_array.append(self.calculate_fitness(final_pos, self.grid.finish_pos))
            print("Fitness: ", fitness_array[i])

            i = i + 1

        # Select parent chromosomes:
        parents = self.roulette_wheel_select(fitness_array)
        print("Parents: ")
        for x in range(len(parents)):
            print(x, " ", parents[x])

        # Apply crossover:
        print(self.crossover(parents))

    # Executes a chromosomes moves and returns the end position:
    def execute_chromosome_moves(self, chromosome):
        # Execute the genes (moves) in single chromosome, and see what path it takes:
        for gene in chromosome:
            CURRENT_MOVE = self.population.gene_to_move(gene)  # Generate next move as array

            # Check for out of bounds or obstacle:
            if self.agent.is_out_of_bounds(CURRENT_MOVE, self.grid.width, self.grid.height) == True:
                continue
            if self.agent.is_hitting_obstacle(CURRENT_MOVE, self.grid.value_array) == True:
                continue

            # Apply move change to agent:
            else:
                self.agent.current_pos[0] = self.agent.current_pos[0] + CURRENT_MOVE[0]
                self.agent.current_pos[1] = self.agent.current_pos[1] + CURRENT_MOVE[1]

            # Check if agent has reached the end point:
            if self.agent.current_pos == self.grid.finish_pos:
                return self.agent.current_pos

        return self.agent.current_pos

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
        parents_indexes = (numpy.random.choice(chromosome_indexes, len(fitness_array), fitness_probabilities))

        # Return the parent chromosomes
        chosen_chromosomes = []
        for index in parents_indexes:
            chosen_chromosomes.append(self.population.chromosomes[index])

        return chosen_chromosomes

    def crossover(self, parents):
        i = 0
        next_population = Chromosome_Population_Class(10, 16)
        new_chromosomes = []
        while i <= 8:
            parent1 = parents.pop(0)
            parent2 = parents.pop(0)

            threshold = int(len(parent1) / 2)
            parent1_half1 = parent1
            del parent1_half1[threshold: len(parent1)]

            parent1_half2 = parent1
            del parent1_half2[0: threshold]

            # parent2_half1 = parent2
            # del parent2_half1[threshold: len(parent2)]
            # parent2_half2 = parent2
            # del parent2_half2[0: threshold]

            print("parent 1 half 1:", parent1_half1)
            print("parent 1 half 2:", parent1_half1)
            # print("parent 1 half 1:", parent1_half1)
            # print("parent 2 half 2:", parent1_half1)

            crossover_rate = 0.7
            if random.uniform(0,1) <= crossover_rate:
                pass
            else:
                # copy chromosomes
                new_chromosomes.append(parent1)
                new_chromosomes.append(parent2)
            i = i + 2
        return new_chromosomes









