import pygame

class windowClass:

    # Constructor:
    def __init__(self, HEIGHT, WIDTH, FILL_COLOR):
        self.height = HEIGHT
        self.width = WIDTH
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(FILL_COLOR)