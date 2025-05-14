class Player:
    def __init__(self, name: str, ships: list, is_bot: bool = False):
        self.name = name
        self.is_bot = is_bot
        self.ships = ships

    # methods tbd