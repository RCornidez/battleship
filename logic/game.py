from .board import Board
from .player import Player
from .ship import Ship

class Game:
    def __init__(self):
        ships = [
            Ship(name="cruiser"),
            Ship(name="submarine"),
            Ship(name="destroyer")
        ]

        self.player_one: Player = Player(name="Player", ships=ships.copy())
        self.player_two: Player = Player(name="Bot", is_bot=True, ships=ships.copy())
        self.active_player: Player = self.player_one
        self.game_state: str = "place_ships"
        self.player_one_state: str = "placing"
        self.player_two_state: str = "placing"

        self.boards: Dict[Player, Board] = {
            self.player_one: Board(),
            self.player_two: Board()
        }

        self.available_shots: List[Tuple[int,int]] = [(row, col) for row in range(Board.size) for col in range(Board.size)]]

    def place_ship(self, player: Player, ship: Ship):
        # Call the board's place_ship method
        self.boards[player].place_ship(ship)

        # check if all the ships are placed for each player
        if len(self.boards[player].ships) == 3:
            if player == self.player_one:
                self.player_one_state = "placed"
            else:
                self.player_two_state = "placed"
        
        # update game state if both players have placed their ships
        if self.player_one_state == "placed" and self.player_two_state == "placed":
            self.game_state = "battle"

    def shoot(self, player: Player, row: int, col: int) -> str:
        
        # assign roles when shooting
        shootee = self.player_two if player == self.player_one else self.player_one
        result = self.boards[shootee].shoot(row, col)

        # remove the shot from available shots for the bot
        if player.is_bot:
            self.available_shots.remove((row, col))

        if result == "miss":
            self.active_player = shootee
        elif result == "hit" and self.boards[shootee].are_all_sunk():
            return "win"
        
        # "hit", "miss", or "already_shot"
        return result