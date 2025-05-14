from .board import Board
from .player import Player
from .ship import Ship

class Game:
    def __init__(self):
        ships = [
            Ship(name="Cruiser", length=3, orientation=["hl","hr","vu","vd"]),
            Ship(name="Submarine", length=3, orientation=["dru","drd","dlu","dld"]),
            Ship(name="Destroyer", length=2, orientation=["hl","hr","vu","vd"]),
        ]

        self.player_one = Player(name="Player", ships=ships.copy())
        self.player_two = Player(name="Bot", is_bot=True, ships=ships.copy())
        self.current_player = self.player_one
        self.board_player_one = Board()
        self.board_player_two = Board()

        # methods tbd