from .cell import Cell
from .ship import Ship
from typing import List


class Board:
    def __init__(self, size: int = 10):
        self.size: int = size
        self.board: List[List[Cell]] = [
            [Cell(row=r, col=c) for c in range(size)] for r in range(size)
        ]
        self.ships: List[Ship] = []

        def _in_bounds(self, row: int, col: int) -> bool:
            # check row is within bounds
            if 0 <= row < self.size:
                # check if column is within bounds
                if 0 <= col < self.size:
                    return True
            return False

        def _free_cell(self, row: int, col: int) -> bool:

            # check if cell is in bounds
            if self._in_bounds(row, col):
                # check if cell has a ship placed there already
                if not self.board[row][col].is_ship:
                    return True
            return False

        def _occupy(self, ship: Ship) -> bool:
            # assign ship coordinates to cells and board
            for row, col in ship.coordinates:
                cell = self.board[row][col]
                cell.is_ship = True
                cell.ship = ship
            self.ships.append(ship)

        def place_ship(self, ship: Ship) -> bool:
            # check if ship is able to be placed, if so, move on to placement below
            for coordinate in ship.coordinates:
                if self._free_cell(coordinate[0], coordinate[1]):
                    continue
                else:
                    return False
            
            # if all cells are free, occupy
            for coordinate in ship.coordinates:
                self._occupy(ship)
            return True

        def shoot(self, row: int, col: int) -> str:
            # call the shoot method of the cell
            return self.board[row][col].shoot()

        def are_all_sunk(self) -> bool:
            # determine if each ship is sunk, exit if any are not
            for ship in self.ships:
                if ship.is_sunk:
                    continue
                else:
                    return False
            return True

        