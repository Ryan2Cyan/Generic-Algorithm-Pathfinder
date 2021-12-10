import os.path
import random
import pygame
import sys

"""
Gene Movement Correlation:
00 - Up
01 - Right
10 - Down
11 - Left
"""


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
            pygame.draw.rect(SCREEN, grid_color(VALUES[row][column]), rect_grid[row][column], 0)  # Grid Fill
            pygame.draw.rect(SCREEN, (10, 30, 200), rect_grid[row][column], 1)  # Grid Lines

# Render grid the AI just moved to:
def draw_move(SCREEN, MOVE):
    return 0

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

def find_start_point(GRID_ARRAY, HEIGHT, WIDTH):
    starting_pos = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if GRID_ARRAY[y][x] == 2:
                starting_pos.append(y)
                starting_pos.append(x)
    return starting_pos

def find_finish_point(GRID_ARRAY, HEIGHT, WIDTH):
    finishing_pos = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if GRID_ARRAY[y][x] == 3:
                finishing_pos.append(y)
                finishing_pos.append(x)
    return finishing_pos

# Convert a gene into a move array:
def gene_to_move(GENE):
    if GENE == '00':  # Up
        return [-1, 0]
    elif GENE == '01':  # Right
        return [0, 1]
    elif GENE == '10':  # Down
        return [1, 0]
    elif GENE == '11':  # Left
        return [0, -1]

# Check if the next move will make the agent out of bounds:
def is_out_of_bounds(CURRENT_POSITION, MOVE_COORDS, WIDTH, HEIGHT):
    if CURRENT_POSITION[0] + MOVE_COORDS[0] < 0 or CURRENT_POSITION[0] + MOVE_COORDS[0] >= HEIGHT:
        return True
    elif CURRENT_POSITION[1] + MOVE_COORDS[1] < 0 or CURRENT_POSITION[1] + MOVE_COORDS[1] >= WIDTH:
        return True
    return False

# Check if the next move will hit an obstacle:
def is_hitting_obstacle(CURRENT_POSITION, MOVE_COORDS, GRID_COORDS):
    NEW_POS = [CURRENT_POSITION[0] + MOVE_COORDS[0], CURRENT_POSITION[1] + MOVE_COORDS[1]]
    if GRID_COORDS[NEW_POS[0]][NEW_POS[1]] == 1:
        return True
    return False

# Check if the next move will land on the end point:
def is_hitting_end(CURRENT_POSITION, MOVE_COORDS, END_POINT):
    NEW_POS = [CURRENT_POSITION[0] + MOVE_COORDS[0], CURRENT_POSITION[1] + MOVE_COORDS[1]]
    if NEW_POS == END_POINT:
        return True
    return False


def main():
    # Initialise Window & Pygame:
    pygame.init()
    WINDOW_HEIGHT = 400
    WINDOW_WIDTH = 400
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.fill((0, 0, 0))
    pygame.display.set_caption("Genetic Algorithm Pathfinder")

    # Read Grid Text File:
    f = extract_grid_from_file("MazeFilesForLab8/Lab8TerrainFile1.txt")
    GRID_WIDTH = f.pop(0)
    GRID_HEIGHT = f.pop(0)
    GRID_VALUES = sort_grid_array(GRID_WIDTH, GRID_HEIGHT, f)

    # Generate first chromosome population:
    all_chromosomes = []
    for x in range(4):
        all_chromosomes.append(gen_chromosome(8))
        print(all_chromosomes[x])

    # Find starting point coords on grid:
    STARTING_POS = find_start_point(GRID_VALUES, GRID_HEIGHT, GRID_WIDTH)
    END_POS = find_finish_point(GRID_VALUES, GRID_HEIGHT, GRID_WIDTH)

    # Set the current coordinates of the chromosome:
    CURRENT_POS = STARTING_POS
    MOVE = gene_to_move('10')
    print("Move :", MOVE)
    print(GRID_VALUES)
    print("Is out of bounds?", is_out_of_bounds(CURRENT_POS, MOVE, GRID_WIDTH, GRID_HEIGHT))
    print("Is hitting obstacle?", is_hitting_obstacle(CURRENT_POS, MOVE, GRID_VALUES))
    print("Current Pos :", CURRENT_POS)
    print("GRID_WIDTH:", GRID_WIDTH)
    print("GRID_HEIGHT:", GRID_HEIGHT)
    i = 0

    # Pathfind for one chromosome:
    for gene in all_chromosomes[0]:
        CURRENT_MOVE = gene_to_move(gene)  # Generate next move array
        print("Current Move:", CURRENT_MOVE)
        if is_out_of_bounds(CURRENT_POS, CURRENT_MOVE, GRID_WIDTH, GRID_HEIGHT) == True:
            print("Out of Bounds.")
            continue
        if is_hitting_obstacle(CURRENT_POS, CURRENT_MOVE, GRID_VALUES) == True:
            print("Hit Obstacle.")
            continue
        else:
            CURRENT_POS[0] = CURRENT_POS[0] + CURRENT_MOVE[0]
            CURRENT_POS[1] = CURRENT_POS[1] + CURRENT_MOVE[1]
            print("Moved to: ", CURRENT_POS)

    # Game Loop:
    while True:
        draw_grid(GRID_WIDTH, GRID_HEIGHT, SCREEN, GRID_VALUES)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main()