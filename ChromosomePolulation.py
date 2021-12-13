import random

class Chromosome_Population_Class:

    # Constructor:
    def __init__(self, POPULATION_SIZE, GENE_LENGTH):
        self.chromosomes = self.gen_population(POPULATION_SIZE, GENE_LENGTH)
        self.fitness_array = []

    # Init population:
    def gen_population(self, POPULATION_SIZE, LENGTH):
        all_chromosomes = []
        for x in range(POPULATION_SIZE):
            all_chromosomes.append(self.gen_chromosome(int(LENGTH / 2)))
        return all_chromosomes

    # Init single bit (as a string):
    def gen_bit(self):
        return str(random.randint(0, 1))

    # Init single gene (2 bits):
    def gen_gene(self):
        return self.gen_bit() + self.gen_bit()

    # Init chromosome:
    def gen_chromosome(self, GENE_COUNT):
        new_chromosome = []
        for x in range(GENE_COUNT):
            new_chromosome.append(self.gen_gene())
        return new_chromosome

    # Convert a gene into a move array:
    def gene_to_move(self, GENE):

        match GENE:
            case '00': # Up
                return [-1, 0]
            case '01': # Right
                return [0, 1]
            case '10': # Down
                return [1, 0]
            case '11': # Left
                return [0, -1]
            case _:
                print("Invalid Gene:")
                return [0, 0]