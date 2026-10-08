class Item:
    """Represents an item in the Mystery Room game."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
