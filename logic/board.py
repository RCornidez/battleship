from .cell import Cell

class Board:
    def __init__(self, size: int = 10):
        self.size = size
        self.board = [
            [Cell(identifier=f"{r},{c}") for c in range(size)] for r in range(size)
        ]

    # remaining methods tbd
    