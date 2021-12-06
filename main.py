import os.path
import random
import pygame
import sys

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

# Init pygame window:
def create_window(height, width):
    BLACK = (0, 0, 0)
    return pygame.display.set_mode((height, width)).fill(BLACK)

# Renders grid to screen:
def draw_grid(WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN, GRID_VALUES):
    blockSize = 20  # Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x + 160, y + 150, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

# Extract Data from Grid File:
def draw_grid_from_file(filepath):
    fp = open(filepath, "r").read().split(" ")
    f2 = []
    for x in range(len(fp)):
        f2.append(int(fp[x]))

    GRID_WIDTH = f2[0]
    GRID_HEIGHT = f2[1]
    print("grid_height :", GRID_HEIGHT)
    print("grid_width :", GRID_WIDTH)
    f2.remove(f2[0])
    f2.remove(f2[1])

    return f2


def main():
    pygame.init()
    WINDOW_HEIGHT = 400
    WINDOW_WIDTH = 400
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill((0, 0, 0))

    # Read Grid Text File:
    f = draw_grid_from_file("MazeFilesForLab8\Lab8TerrainFile1.txt")
    print(f)

    # while True:
    #     draw_grid(60, 60, SCREEN, (200, 200, 200))
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #     pygame.display.update()

    all_chromosomes = []

    # Generate chromosomes:
    # for x in range(20):
    #     all_chromosomes.append(gen_chromosome(5))
    #     print(all_chromosomes[x])



    # Extract data and assign to correct variables:

main()