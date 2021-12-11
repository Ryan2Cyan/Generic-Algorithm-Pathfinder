import os.path
import pygame
import sys

class windowClass:

    # Constructor:
    def __init__(self, height, width, fill_color):
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill(fill_color)