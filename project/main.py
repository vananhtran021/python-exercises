import random

from game.item import Item
from game.room import Room
from game.player import Player


def guess_number(number):
    guess = int(input("Guess a number from 1 to 10: "))

    if guess == number:
        print("Correct! You guessed the number!")
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")


def get_hint(number):
    print("Hint: The number is between 1 and 10.")


def new_game():
    print("A new number has been chosen!")
    return random.randint(1, 10)


def show_inventory(player):
    print("\nInventory")

    if len(player.items) == 0:
        print("Your inventory is empty.")
    else:
        for item in player.items:
            print("-", item)


def main():
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    if age < 12:
        print("You are a minor. The game is shutting down.")
        return

    print(f"Welcome, {name}!")

    # Create items
    key = Item("Key", 0.2)
    book = Item("Book", 1.0)
    coin = Item("Coin", 0.1)

    # Create rooms
    bedroom = Room("Bedroom", key)
    kitchen = Room("Kitchen", book)
    garden = Room("Garden", coin)

    # Create player
    player = Player(name, bedroom)

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
        print("lopeta - Quit the game")

        command = input("Enter command: ")

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

        elif command == "lopeta":
            print("Game over. Goodbye!")
            break

        else:
            print("Unknown command.")


main()