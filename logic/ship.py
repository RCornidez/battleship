class Ship:
    def __init__ (self, name: str, length: int):
        self.name = name
        self.length = length
        self.is_sunk = False
        self.coordinates = []
        self.coordinates_shot = []

    def set_coordinates(self, coordinates: list):
        self.coordinates = coordinates
    
    def got_hit(self, coordinate: str):
        self.coordinates_shot.append(coordinate)
        # tbd determine if the ship is sunk
