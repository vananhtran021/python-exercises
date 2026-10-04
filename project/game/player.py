class Player:
    def __init__(self, name: str, location):
        self.name = name
        self.items = []
        self.location = location

    def move(self, destination):
        self.location = destination
        print(f"You moved to {destination.name}.")

    def collect_item(self):
        if self.location.item is not None:
            item = self.location.item
            self.items.append(item)
            self.location.item = None

            print(f"{item.name} was added to your inventory.")
        else:
            print("There is no item in this room.")