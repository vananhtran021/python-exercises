class Player:
    """Represents the player."""

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        self.inventory = []
        self.score = 0

    def move(self, room):
        """Move the player to a connected room."""
        if room in self.location.connections:
            self.location = room
            print(f"\nYou moved to {room.name}.")
            return True

        print("\nYou cannot move directly to that room.")
        return False

    def collect_item(self):
        """Collect the item from the current room."""
        if self.location.item is None:
            print("\nThere is no item to collect here.")
            return None

        item = self.location.item

        self.inventory.append(item)
        self.location.item = None

        print(f"\nYou collected: {item.name}")
        self.score += 5
        print("You earned 5 points!")

        return item

    def get_item_quantity(self, item_name):
        """Count how many of a specific item the player has."""
        quantity = 0

        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                quantity += 1

        return quantity

    def get_total_items(self):
        """Return the total number of items collected."""
        return len(self.inventory)

    def has_item(self, item_name):
        """Check whether the player has a specific item."""
        return self.get_item_quantity(item_name) > 0

    def show_inventory(self):
        """Display the player's inventory."""
        print("\n========== INVENTORY ==========")

        if not self.inventory:
            print("Your inventory is empty.")
            print("===============================")
            return

        item_names = []

        for item in self.inventory:
            if item.name not in item_names:
                item_names.append(item.name)

        for item_name in item_names:
            quantity = self.get_item_quantity(item_name)
            print(f"- {item_name} x{quantity}")

        print(f"\nTotal items: {self.get_total_items()}")
        print("===============================")

    def show_status(self):
        """Display the player's current status."""
        print("\n========== PLAYER STATUS ==========")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Current room: {self.location.name}")
        print(f"Score: {self.score}")
        print(f"Total items: {self.get_total_items()}")
        print("===================================")