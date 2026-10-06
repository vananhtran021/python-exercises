import random
import os

from game.item import Item
from game.room import Room
from game.player import Player


def read_file(filename):
    file_path = os.path.join(os.path.dirname(__file__), filename)

    with open(file_path, "r") as file:
        return file.read()


def save_game(player):
    file_path = os.path.join(os.path.dirname(__file__), "savegame.txt")

    with open(file_path, "w") as file:
        file.write(player.name + "\n")
        file.write(player.location.name + "\n")

    print("Game saved successfully!")


def load_game():
    file_path = os.path.join(os.path.dirname(__file__), "savegame.txt")

    try:
        with open(file_path, "r") as file:
            name = file.readline().strip()
            room_name = file.readline().strip()

        print("Saved game found!")
        return name, room_name

    except FileNotFoundError:
        print("No saved game found.")
        return None


def guess_number(number):
    guess = int(input("Guess a number from 1 to 10: "))

    if guess == number:
        print("Correct! You guessed the number!")
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")


def get_hint(number):
    print(f"Hint: the number is between 1 and 10.")


def new_game():
    number = random.randint(1, 10)
    print("A new number has been generated!")
    return number


def show_inventory(player):
    if player.inventory:
        print("\nYour inventory:")
        for item in player.inventory:
            print(f"- {item.name}")
    else:
        print("\nYour inventory is empty.")


def main():
    # Read introduction and instructions from text files
    print(read_file("intro.txt"))
    print()
    print(read_file("instructions.txt"))
    print()

    # Create items
    key = Item("Key", 0.2)
    book = Item("Book", 1.0)
    coin = Item("Coin", 0.1)

    # Create rooms
    bedroom = Room("Bedroom", key)
    kitchen = Room("Kitchen", book)
    garden = Room("Garden", coin)

    # Choose new game or continue
    choice = input(
        "Do you want to start a (N)ew game or (C)ontinue? "
    ).lower()

    if choice == "c":
        saved_game = load_game()

        if saved_game:
            name, room_name = saved_game
            age = int(input("How old are you? "))

            # Restore player's location
            if room_name == "Bedroom":
                starting_room = bedroom
            elif room_name == "Kitchen":
                starting_room = kitchen
            elif room_name == "Garden":
                starting_room = garden
            else:
                starting_room = bedroom

        else:
            print("Starting a new game...")
            name = input("What is your name? ")
            age = int(input("How old are you? "))
            starting_room = bedroom

    else:
        name = input("What is your name? ")
        age = int(input("How old are you? "))
        starting_room = bedroom

    # Check age
    if age < 12:
        print("You are a minor. The game is shutting down.")
        return

    print(f"Welcome, {name}!")

    # Create player
    player = Player(name, starting_room)

    # Create random number
    number = random.randint(1, 10)

    while True:
        print("\nMain Menu")
        print("arvaa - Guess the number")
        print("vihje - Get a hint")
        print("uusi - Start a new game")
        print("liiku - Move to another room")
        print("lisaa - Collect item")
        print("reppu - Show inventory")
        print("huone - Show current room")
        print("tallenna - Save the game")
        print("lopeta - Quit the game")

        command = input("Enter command: ").lower()

        if command == "arvaa":
            guess_number(number)

        elif command == "vihje":
            get_hint(number)

        elif command == "uusi":
            number = new_game()

        elif command == "liiku":
            print("\nWhere do you want to go?")
            print("1 - Bedroom")
            print("2 - Kitchen")
            print("3 - Garden")

            destination = input("Choose a room: ")

            if destination == "1":
                player.move(bedroom)
            elif destination == "2":
                player.move(kitchen)
            elif destination == "3":
                player.move(garden)
            else:
                print("Unknown room.")

        elif command == "lisaa":
            player.collect_item()

        elif command == "reppu":
            show_inventory(player)

        elif command == "huone":
            print(f"\nYou are currently in the {player.location.name}.")

            if player.location.item is not None:
                print(f"There is a {player.location.item.name} here.")
            else:
                print("There is no item here.")

        elif command == "tallenna":
            save_game(player)

        elif command == "lopeta":
            print("Game over. Goodbye!")
            break

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()