import random

class Chromosome_Population_Class:

    # Constructor:
    def __init__(self, population_size, gene_length):
        self.chromosomes = self.gen_population(population_size, gene_length)
        self.fitness_array = []

    # Init population:
    def gen_population(self, pop_size, length):
        all_chromosomes = []
        for x in range(pop_size):
            all_chromosomes.append(self.gen_chromosome(int(length / 2)))
        return all_chromosomes

    # Init single bit (as a string):
    def gen_bit(self):
        return str(random.randint(0, 1))

    # Init single gene (2 bits):
    def gen_gene(self):
        return self.gen_bit() + self.gen_bit()

    # Init chromosome:
    def gen_chromosome(self, gene_count):
        new_chromosome = []
        for x in range(gene_count):
            new_chromosome.append(self.gen_gene())
        return new_chromosome

    # Convert a gene into a move array:
    def gene_to_move(self, GENE):
        if GENE == '00':  # Up
            return [-1, 0]
        elif GENE == '01':  # Right
            return [0, 1]
        elif GENE == '10':  # Down
            return [1, 0]
        elif GENE == '11':  # Left
            return [0, -1]