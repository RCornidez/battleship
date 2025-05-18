from .ship import ORIENTATION, SHIPS
import random

class Board:
    EMPTY = 0
    SHIP = 1
    HIT = 2
    MISS = 3

    def __init__(self, size):
        self.size = size
        self.grid = [[self.EMPTY] * size for i in range(size)]

    def is_available(self, row, col, direction, length):
        dr, dc = ORIENTATION[direction]
        ship_coords = [(row + i * dr, col + i * dc) for i in range(length)]

        # Check if coordinates are within the board
        if any(not (0 <= x < self.size and 0 <= y < self.size) for x, y in ship_coords):
            return False, []

        # Check if the coordinates are empty
        if any(self.grid[x][y] != self.EMPTY for x, y in ship_coords):
            return False, []

        # Coordinates are valid
        return True, ship_coords

    def is_cell_valid(self, row, col):
        # check if cell is within the board
        if not (0 <= row < self.size and 0 <= col < self.size):
            return False, []
        # check if cell is not already shot
        if self.grid[row][col] == self.HIT or self.grid[row][col] == self.MISS:
            return False, []

        # cell is valid
        return True, [row, col]

    def place_ship(self, row, col, direction, length):
        # validity check
        is_valid, ship_coords = self.is_available(row, col, direction, length)

        if not is_valid:
            return False
        for r, c in ship_coords:
            self.grid[r][c] = self.SHIP
        return True

    def randomly_place_ships(self):
        # try and place ships until all ships are successfully placed
        for i, length, directions in SHIPS:
            placed = False
            while not placed:
                row = random.randrange(self.size)
                col = random.randrange(self.size)
                direction = random.choice(directions)
                placed = self.place_ship(row, col, direction, length)
    
    def handle_shot(self, row, col):
        # Mark as shot if the cell has a ship
        if self.grid[row][col] == self.SHIP:
            self.grid[row][col] = self.HIT
            return True
        # Mark as miss if the cell is empty
        elif self.grid[row][col] == self.EMPTY:
            self.grid[row][col] = self.MISS
            return False

        # Do nothing if the cell is not marked as ship or empty
        return None

    def check_ships(self):
        # check if there are any ship cells left on the board
        for row in self.grid:
            for cell in row:
                if cell == self.SHIP:
                    return False

        # All ships are sunk
        return True

