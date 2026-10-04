class Item:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"
key = Item("Key", 0.2)
book = Item("Book", 1.0)