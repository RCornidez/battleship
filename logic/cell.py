class Cell:
    row: int
    col: int
    is_shot: bool = False
    is_ship: bool = False
    ship: Ship = None

    def shoot(self):
        # Check if already shot
        if self.is_shot:
            return "already_shot"

        # Set cell to shot state
        self.is_shot = True

        # Check if ship is present, if so, register hit
        if self.is_ship:
            self.ship.register_hit((self.row, self.col))
            return "hit"

        # if no ship, return "miss"
        return "miss"
            
    