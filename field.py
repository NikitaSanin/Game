import random
from utils import load_level_matrix


class GameField:
    def __init__(self, filename):
        self.grid = load_level_matrix("levels/" + filename)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def get_valid_spawn(self, used_positions):
        while True:
            x = random.randint(1, self.cols - 2)
            y = random.randint(1, self.rows - 2)
            if self.grid[y][x] == 0 and (x, y) not in used_positions:
                return x, y

    def is_wall(self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            return self.grid[y][x] == 1
        return True