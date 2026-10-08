class Room:
    """Represents a room in the Mystery Room game."""

    def __init__(self, name, description, item=None):
        self.name = name
        self.description = description
        self.item = item
        self.connections = []

    def add_connection(self, room):
        """Connect this room to another room."""
        self.connections.append(room)

    def show_room(self):
        """Display information about the current room."""
        print(f"\n========== {self.name.upper()} ==========")
        print(self.description)

        if self.item is not None:
            print(f"\nYou found: {self.item.name}")
        else:
            print("\nThere is no item here.")

        if self.connections:
            print("\nYou can move to:")
            for number, room in enumerate(self.connections, start=1):
                print(f"{number}. {room.name}")

        print("================================")