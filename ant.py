#!/usr/bin/env python3

import random
import time

UP = [0, 1]  # [0, 1] means move up in the grid
DOWN = [0, -1]  # [0, -1] means move down in the grid
LEFT = [-1, 0]  # [-1, 0] means move left in the grid
RIGHT = [1, 0]  # [1, 0] means move right in the grid

directions = [UP, DOWN, LEFT, RIGHT]


def rotate_clockwise(vec):
    # Rotate vector 90 degrees clockwise
    # [x, y] -> [y, -x]
    # Example: [1, 0] -> [0, -1]  RIGHT -> DOWN
    #          [0, -1] -> [-1, 0] DOWN -> LEFT
    #          [-1, 0] -> [0, 1] LEFT -> UP
    #          [0, -1] -> [-1, 0] DOWN -> LEFT
    return [vec[1], -vec[0]]


def rotate_counterclock(vec):
    return [-vec[1], vec[0]]


class LangtonAnt:
    """
    Langton's Ant Simulator
    """

    BLACK = "X"  # 0 means black cell
    WHITE = "O"  # 1 means white cell

    def __init__(self, grid_size):
        self.grid_size = grid_size
        # Initialize the grid with white cells
        self.grid = [
            [LangtonAnt.WHITE for j in range(self.grid_size)]
            for i in range(self.grid_size)
        ]
        self._initialize_ant(grid_size)  # Initialize the ant's position and direction

    def _initialize_ant(self, size):
        """Initialize the ant's position and direction.

        Args:
            size (_type_): Size of the grid (size x size).
        """
        # Initialize the ant's position at the center of the grid
        # ant_r is the row index, ant_c is the column index
        self.ant_r, self.ant_c = int(self.grid_size / 2), int(self.grid_size / 2)
        # randomize initial direction
        self.direction = random.choice(directions)
        print(self.direction)

    def run(self, epoch=10):
        for i in range(epoch):
            print("Epoch ==> {} :: BLACK:0 :: WHITE:1".format(i))
            print("=" * 40)
            print(self)  # Print the current state of the grid
            self.step()
            time.sleep(0.1)
            print("=" * 40)
        print("Final state...")
        print("=" * 40)
        print(self)

    def step(self):
        """
        Run for single time step.
        Transition from time t to (t+1)
        """
        r, c = self.ant_r, self.ant_c  # Get current position of the ant
        # Check if the ant is out of bounds
        if r < 0 or r >= self.grid_size or c < 0 or c >= self.grid_size:
            print("Ant is out of bounds! Resetting position.")
            self._initialize_ant(self.grid_size)
            return
        if self.grid[r][c] == LangtonAnt.WHITE:
            self.direction = rotate_counterclock(self.direction)
            self.grid[r][c] = LangtonAnt.BLACK
        else:
            self.direction = rotate_clockwise(self.direction)
            self.grid[r][c] = LangtonAnt.WHITE

        self.ant_r -= self.direction[1]
        self.ant_c += self.direction[0]

    def __str__(self):
        r, c = self.ant_r, self.ant_c
        curr = self.grid[r][c]
        self.grid[r][c] = "*"
        ret = ""
        for row in self.grid:
            for x in row:
                ret += str(x) + " "
            ret += "\n"
        self.grid[r][c] = curr
        return ret.strip()


def main():
    ant = LangtonAnt(50)
    ant.run(500)


if __name__ == "__main__":
    main()
