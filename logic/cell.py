class Cell:
    def __init__(self, identifier: str):
        self.identifier = identifier
        self.is_shot = False
        self.is_ship = False

    def shot(self):
        self.is_shot = True
    