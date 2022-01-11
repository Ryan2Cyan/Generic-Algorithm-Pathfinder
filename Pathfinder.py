import pygame
import random
import numpy
from Grid import Grid_Class
from ChromosomePolulation import Chromosome_Population_Class
from Agent import Agent_Class


class Pathfinder_Class:

    # Constructor - Note: the param 'FILE_CONTENTS' must not include the first 2 digits of the grid array (w and h):
    def __init__(self, POPULATION_SIZE, CHROMOSOME_LENGTH, GRID_WIDTH, GRID_HEIGHT, FILE_CONTENTS,
                 SCREEN):
        self.population = Chromosome_Population_Class(POPULATION_SIZE, CHROMOSOME_LENGTH)
        self.grid = Grid_Class(GRID_WIDTH, GRID_HEIGHT, FILE_CONTENTS, SCREEN)
        self.agent = Agent_Class(self.grid.start_pos)
        self.current_gen = 0
        self.current_chromosome = 0
        self.population_size = POPULATION_SIZE
        self.chromosome_length = CHROMOSOME_LENGTH

    # This function executes the moves of all chromosomes in a population
    def execute_population(self):
        found_path = False
        while found_path == False:
            i = 0
            fitness_array = []
            self.agent.redundant_steps = 1
            self.agent.path_length = 0
            # For each chromosome in the current generation:
            for chromosome in self.population.chromosomes:

                START_POS = self.grid.start_pos  # where the agent starts
                GOAL_POS = self.grid.finish_pos  # the end goal
                self.agent.redundant_steps = 1 # reset amount of redundant steps

                # Reset agent to start pos:
                self.agent.current_pos[0] = START_POS[0]
                self.agent.current_pos[1] = START_POS[1]

                # Execute all chromosome moves and return the final position of the agent:
                valid_moves = self.execute_chromosome_moves(chromosome, GOAL_POS)

                self.agent.path_length = len(valid_moves)
                if self.agent.current_pos == GOAL_POS:
                    self.current_chromosome = self.current_chromosome + (i + 1)
                    found_path = True
                    self.draw_path(valid_moves, self.grid.start_pos)
                    return valid_moves

                # Calc this chromosome's fitness and add to the fitness array:
                fitness_array.append(self.calculate_fitness(self.agent.current_pos, GOAL_POS))

                i = i + 1

            # Select parent chromosomes:
            parents = self.roulette_wheel_select(fitness_array)

            # Apply crossover:
            self.population.chromosomes = self.crossover(parents)

            # Apply mutation:
            self.population.chromosomes = self.mutation(self.population.chromosomes)

            # Increment values to keep track of generation and chromosomes:
            self.current_chromosome = self.current_chromosome + len(self.population.chromosomes)
            self.current_gen = self.current_gen + 1


    # Executes a chromosomes moves and returns the end position:
    def execute_chromosome_moves(self, CHROMOSOME, GOAL_POS):

        index = 0
        valid_moves = []  # Array with redundant moves removed.

        # Execute the genes (moves) in single chromosome, and see what path it takes:
        for GENE in CHROMOSOME:

            CURRENT_MOVE = self.population.gene_to_move(GENE)  # Generate next move as array

            # Check for out of bounds or obstacle:
            if self.agent.is_out_of_bounds(CURRENT_MOVE, self.grid.width, self.grid.height) == True:
                self.agent.redundant_steps = self.agent.redundant_steps + 1
                continue
            if self.agent.is_hitting_obstacle(CURRENT_MOVE, self.grid.value_array) == True:
                self.agent.redundant_steps = self.agent.redundant_steps + 1
                continue

            # Apply move change to agent:
            else:
                self.agent.current_pos[0] = self.agent.current_pos[0] + CURRENT_MOVE[0]
                self.agent.current_pos[1] = self.agent.current_pos[1] + CURRENT_MOVE[1]
                valid_moves.append(GENE)

        return valid_moves

    # Calculates the fitness of a single chromosome:
    def calculate_fitness(self, AGENT_CURRENT_POS, GOAL_POS):

        # Calculate fitness modifiers for path len:
        path_len = 0
        if self.agent.path_length != 0:
            path_len = (1 / self.agent.path_length + 1)

        # Calculate fitness modifiers for redundant steps:
        redundant_steps = (1 / self.agent.redundant_steps + 1)

        # Calculate fitness modifiers for offset from goal pos:
        y_offset = abs(GOAL_POS[0] - AGENT_CURRENT_POS[0])
        x_offset = abs(GOAL_POS[1] - AGENT_CURRENT_POS[1])
        offset = 1 / (x_offset + y_offset + 1)

        # Add them together for the fitness:
        fitness = path_len + redundant_steps + offset

        return fitness

    # Roulette wheel chromosome selector - returns an array of indexes for chosen parent chromosomes:
    def roulette_wheel_select(self, FITNESS_ARRAY):
        # Calculate total fitness:
        total_fitness = round(sum(FITNESS_ARRAY), 2)

        # Calculate probability for each fitness:
        fitness_probabilities = []
        for FITNESS_VALUE in FITNESS_ARRAY:
            fitness_probabilities.append(round((FITNESS_VALUE / total_fitness) * 100, 2))

        # Make array of indexes to reference what chromosomes will be picked:
        chromosome_indexes = [x for x in range(len(FITNESS_ARRAY))]

        # Choose parent chromosomes:
        parents_indexes = (numpy.random.choice(chromosome_indexes, len(FITNESS_ARRAY), fitness_probabilities))

        # Return the parent chromosomes
        chosen_chromosomes = []
        for index in parents_indexes:
            chosen_chromosomes.append(self.population.chromosomes[index])

        return chosen_chromosomes

    # Takes in an array of 'parent chromosomes' and applies crossover - returning a new generation:
    def crossover(self, parents):
        i = 0
        next_population = Chromosome_Population_Class(self.population_size, self.chromosome_length)
        new_chromosomes = []
        NUM_OF_OFFSPRING = len(parents)

        # for each chromosome pair:
        while i < NUM_OF_OFFSPRING:

            # Get the parent pair:
            PARENT1 = parents.pop(0)
            PARENT2 = parents.pop(0)

            # Crossover rate (how frequent crossover will occur):
            CROSSOVER_RATE = 1
            # Index crossover that crossover will occur:
            MIDWAY_INDEX = int(len(PARENT1) / 2)

            if random.uniform(0, 1) <= CROSSOVER_RATE:

                # Apply crossover (cross genes of parents):
                child1 = []
                child2 = []

                for x in range(len(PARENT1)):
                    if x < MIDWAY_INDEX:
                        child1.append(PARENT1[x])
                        child2.append(PARENT2[x])
                    else:
                        child1.append(PARENT2[x])
                        child2.append(PARENT1[x])
                new_chromosomes.append(child1)
                new_chromosomes.append(child2)
            else:
                # No crossover (copy the chromosomes):
                new_chromosomes.append(PARENT1)
                new_chromosomes.append(PARENT2)
            i = i + 2

        return new_chromosomes

    # Takes an array of chromosomes and applies mutation - returning the mutated chromosomes:
    def mutation(self, new_population):
        MUTATION_RATE = 0.03

        # Loop through all genes and randomise some of them depending on the mutation rate:
        for chromosome in range(len(new_population)):
            for gene in range(len(new_population[chromosome])):
                if random.uniform(0, 1) <= MUTATION_RATE:
                    new_population[chromosome][gene] = self.population.gen_gene()

        return new_population

    # Draws final path to grid:
    def draw_path(self, CHROMOSOME, start_pos):
        self.agent.current_pos[0] = start_pos[0]
        self.agent.current_pos[1] = start_pos[1]

        # Execute the genes (moves) in single chromosome, and see what path it takes:
        for GENE in CHROMOSOME:
            CURRENT_MOVE = self.population.gene_to_move(GENE)  # Generate next move as array

            self.agent.current_pos[0] = self.agent.current_pos[0] + CURRENT_MOVE[0]
            self.agent.current_pos[1] = self.agent.current_pos[1] + CURRENT_MOVE[1]
            if self.grid.value_array[self.agent.current_pos[0]][self.agent.current_pos[1]] == 0:
                self.grid.value_array[self.agent.current_pos[0]][self.agent.current_pos[1]] = 4












