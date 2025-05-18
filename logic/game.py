from .board import Board
from .ship import SHIPS, ORIENTATION
import random

class Game:
    def __init__(self, size=10):
        # setup boards
        self.player_board = Board(size)
        self.bot_board = Board(size)
        self.bot_board.randomly_place_ships()

        # setup game state
        self.size = size
        self.state = 'placing'
        self.ship_index = 0
        self.ship_orientation = SHIPS[0][2][0]
        self.player_turn = True
        self.bot_targets = []

    def player_place_ship(self, row, col, orientation):
        name, length, directions = SHIPS[self.ship_index]

        # exit if not a valid orientation
        if orientation not in directions:
            return False

        # place the ship on the player's board
        placed_ship = self.player_board.place_ship(row, col, orientation, length)

        # exit if not successfully placed
        if not placed_ship:
            return False

        self.ship_index += 1

        if self.ship_index == len(SHIPS):
            self.state = 'playing'
        else:
            self.ship_orientation = SHIPS[self.ship_index][2][0]

        # Successfully placed the ship
        return True

    def player_shot(self, row, col):
        shot = self.bot_board.handle_shot(row, col)

        if shot is None:
            return None
        if shot:
            if self.bot_board.check_ships():
                return 'win'
            return 'hit'
        else:
            self.player_turn = False
            return 'miss'

    def bot_shot(self):

        potential_shots = [
            (r,c)
            for r in range(self.size)
            for c in range(self.size)
            if self.player_board.grid[r][c] in (Board.EMPTY, Board.SHIP)
        ]

        while True:
            # Aim for a target if available
            if self.bot_targets:
                r, c = self.bot_targets.pop(0)
            # Otherwise, select a random shot
            else:
                # randomly select
                r, c = random.choice(potential_shots)
            
            shot_result = self.player_board.handle_shot(r,c)
        
            # already shot, try again
            if shot_result is None:
                continue

            # if hit, record neighbors for strategic targeting
            if shot_result:
                for dr, dc in ORIENTATION.values():
                    neighbor_row = r + dr
                    neighbor_col = c + dc

                    # validate the neighbors
                    valid, _ = self.player_board.is_cell_valid(neighbor_row, neighbor_col)
                    if valid and (neighbor_row, neighbor_col) not in self.bot_targets:
                        self.bot_targets.append((neighbor_row, neighbor_col))

                # Check if all player's ships have been sunk
                if self.player_board.check_ships():
                    return 'lose'

                # Bot gets another turn after a hit
                return 'hit'
            
            # miss, switch turns
            else:
                self.player_turn = True
                return 'miss'
                

                for row in range(self.size):
                    for col in range(self.size):
                        cell = self.player_board.grid[row][col]
                        if cell == Board.EMPTY or cell == Board.SHIP:
                            potential_shots.append((row, col))

                # randomly select and fire a shot
                r, c = random.choice(potential_shots)
                shot_result = self.player_board.handle_shot(r,c)


                
                
                    


        
