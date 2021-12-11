import os.path
import pygame
import sys

class fileReaderClass:

    # Constructor:
    def __init__(self, file_path):
        self.contents_of_file = self.extract_grid_from_file(file_path)

    # Extract Data from Grid File:
    def extract_grid_from_file(self, filepath):
        fp = open(filepath, "r").read().split(" ")
        f2 = []
        for x in range(len(fp)):
            f2.append(int(fp[x]))
        return f2
