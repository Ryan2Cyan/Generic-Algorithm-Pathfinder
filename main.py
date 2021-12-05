import random


# Init single bit (as a string):
def gen_bit():
    return str(random.randint(0, 1))


# Init single gene (2 bits):
def gen_gene():
    return gen_bit() + gen_bit()


# Init chromosome:
def gen_chromosome(gene_count):
    new_chromosome = []
    for x in range(gene_count):
        new_chromosome.append(gen_gene())
    return new_chromosome


# Extract Data from Grid File:
def extract_grid_data(filepath):
    fp = open(filepath, "r").read().split(" ")
    f2 = []
    for x in range(len(fp)):
        f2.append(int(fp[x]))
    return f2


all_chromosomes = []

# Generate chromosomes:
for x in range(20):
    all_chromosomes.append(gen_chromosome(5))
    print(all_chromosomes[x])

# # Read Grid Text File:
# f = extract_grid_data("Lab8TerrainFile1.0.txt")

# Extract data and assign to correct variables:
