class Ship:
    def __init__(self, name: str):
        self.name = name
        self.coordinates: List[Tuple[int,int]] = []
        self.hits: Set[Tuple[int,int]] = set()
        self.is_sunk: bool = False

   def register_hit(self, coordinate: Tuple[int,int]):
        # add shot to the hits set
        self.hits.add(coordinate)

        # check ship's sunk status
        if self.coordinates == self.hits:
            self.is_sunk = True