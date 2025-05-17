from .ship import Ship
from typing import List

class Player:
    def __init__(self, name: str, ships: List[Ship], is_bot: bool = False):
        self.name: str = name
        self.is_bot: bool = is_bot
        self.ships: List[Ship] = ships