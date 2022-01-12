# Pathfinder.py
# Compiler: Python 3.10

import pygame
import random
import numpy
from Grid import Grid_Class
from Agent import Agent_Class
from queue import PriorityQueue
from Node import Node_Class

class A_Star_Pathfinder_Class:

    # Constructor - Note: the param 'FILE_CONTENTS' must not include the first 2 digits of the grid array (w and h):
    def __init__(self, GRID_WIDTH, GRID_HEIGHT, FILE_CONTENTS,
                 SCREEN):
        self.grid = Grid_Class(GRID_WIDTH, GRID_HEIGHT, FILE_CONTENTS, SCREEN)
        self.agent = Agent_Class(self.grid.start_pos)

    def execute_a_star(self):

        # Create start and end nodes:
        start_node = Node_Class(None, self.grid.start_pos)
        start_node.g = start_node.h = start_node.f = 0

        end_node = Node_Class(None, self.grid.finish_pos)
        end_node.g = end_node.h = end_node.f = 0

        # Initialise open and closed lists:
        open_list = []
        closed_list = []

        # Add start node:
        open_list.append(start_node)

        test_index = 0
        # Loop until you find the end:
        while test_index < 20:

            # Get current node:
            current_node = open_list[0]
            current_index = 0
            print("current_node: ", current_node.position)
            print("current_index:", current_index)

            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current node off of open list, add to closed list:
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal:
            if current_node == end_node:
                print("found path!")
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1] # Return reversed path

            # Get neighbors:
            neighbors = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Neighbor nodes (4-directions):

                # Get neighbor position:
                neighbor_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Make sure within range:
                if neighbor_position[0] > (self.grid.height) - 1 or neighbor_position[0] < 0\
                        or neighbor_position[1] > (self.grid.width) - 1 or neighbor_position[1] < 0:
                    continue

                # Make sure walkable terrain:
                if self.grid.value_array[neighbor_position[0]][neighbor_position[1]] == 1:
                    print("continue")
                    continue

                # Create new node:
                new_node = Node_Class(current_node, neighbor_position)
                print("new nodes:", new_node.position)

                # Append:
                neighbors.append(new_node)

            final_nodes = []
            # Loop through neighbors:
            for node in neighbors:
                print("neighbor: ",node.position)

                # Neighbor on the closed list:
                for closed_neighbor in closed_list:
                    if node == closed_neighbor:
                        print("On closed list")
                        continue

                # Create the f, g, and h costs:
                node.g = current_node.g + 1
                print("G:", node.g)
                node.h = self.heuristic(node.position, self.grid.finish_pos)
                print("H:", node.h)
                node.f = node.g + node.h
                print("F:", node.f)

                # Node is already in open list:
                for open_node in open_list:
                    if node == open_node and node.g > open_node.g:
                        print("on open list")
                        continue

                # Add child to open list:
                final_nodes.append(node)
                test_index = test_index + 1

            # Add node with lowest f-cost to open list:


            print(" ")

    # Calculates the distance between two nodes (in Manhatten Distance):
    def heuristic(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)



