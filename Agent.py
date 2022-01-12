# Agent.py
# Compiler: Python 3.10

class Agent_Class:

    # Constructor:
    def __init__(self, STARTING_POS):
        self.current_pos = [[],[]]
        self.starting_pos = STARTING_POS
        self.path_length = 0
        self.redundant_steps = 0

    # Check if the next move will make the agent out of bounds:
    def is_out_of_bounds(self, MOVE_COORDS, WIDTH, HEIGHT):
        if self.current_pos[0] + MOVE_COORDS[0] < 0 or self.current_pos[0] + MOVE_COORDS[0] >= HEIGHT:
            return True
        elif self.current_pos[1] + MOVE_COORDS[1] < 0 or self.current_pos[1] + MOVE_COORDS[1] >= WIDTH:
            return True
        return False

    # Check if the next move will hit an obstacle:
    def is_hitting_obstacle(self, MOVE_COORDS, GRID_COORDS):
        NEW_POS = [self.current_pos[0] + MOVE_COORDS[0], self.current_pos[1] + MOVE_COORDS[1]]
        if GRID_COORDS[NEW_POS[0]][NEW_POS[1]] == 1:
            return True
        return False

