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
def draw_grid(WIDTH, HEIGHT, SCREEN, VALUES):

    blockSize = 40  # Set the size of the grid block

    rect_grid = []
    for x in range(0, HEIGHT * blockSize, blockSize):
        for y in range(0, WIDTH * blockSize, blockSize):
            rect = pygame.Rect(y, x, blockSize, blockSize)
            rect_grid.append(rect)

    # 2-D array of Grid Squares
    rect_grid = sort_grid_array(WIDTH, HEIGHT, rect_grid)

    # Render Grid Squares
    for row in range(HEIGHT):
        for column in range(WIDTH):
            print(grid_color(VALUES[row][column]))
            pygame.draw.rect(SCREEN, grid_color(VALUES[row][column]), rect_grid[row][column], 0)
# Switch for Grid Square Color:
def grid_color(grid_value):
    if grid_value == 0:
        return (255, 255, 255)
    elif grid_value == 1:
        return (0, 0, 0)
    elif grid_value == 2:
        return (10, 200, 30)
    elif grid_value == 3:
        return (10, 40, 200)
# Extract Data from Grid File:
def extract_grid_from_file(filepath):
    fp = open(filepath, "r").read().split(" ")
    f2 = []
    for x in range(len(fp)):
        f2.append(int(fp[x]))
    return f2
# Sorts Grid Values into a 2-D Array
def sort_grid_array(WIDTH, HEIGHT, FILE_DATA_ARRAY):
    GRID_VALUES = []
    i = 0

    # create 2-D grid
    for row in range(HEIGHT):
        GRID_VALUES.append([])
        for column in range(WIDTH):
            GRID_VALUES[row].append(0)
            GRID_VALUES[row][column] = FILE_DATA_ARRAY[i]
            i = i + 1
    return GRID_VALUES

def main():

    pygame.init()
    WINDOW_HEIGHT = 400
    WINDOW_WIDTH = 400
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.fill((0, 0, 0))
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption("Genetic Algorithm Pathfinder")

    # Read Grid Text File:
    f = extract_grid_from_file("MazeFilesForLab8\Lab8TerrainFile1.txt")
    GRID_WIDTH = f.pop(0)
    GRID_HEIGHT = f.pop(0)
    GRID_VALUES = sort_grid_array(GRID_WIDTH, GRID_HEIGHT, f)

    # Generate chromosomes:
    all_chromosomes = []
    # for x in range(20):
    #     all_chromosomes.append(gen_chromosome(5))
    #     print(all_chromosomes[x])

    # Game Loop:
    while True:
        draw_grid(GRID_WIDTH, GRID_HEIGHT, SCREEN, GRID_VALUES)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()