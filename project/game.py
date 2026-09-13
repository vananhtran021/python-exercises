import random

inventory = []


def guess_number(number):
    guess = int(input("Guess a number from 1 to 10: "))

    if guess == number:
        print("Correct! You guessed the number!")
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")


def get_hint(number):
    print(f"Hint: The number is between 1 and 10.")


def new_game():
    print("A new number has been chosen!")
    return random.randint(1, 10)


def add_item():
    item = input("What item do you want to add to your inventory? ")
    inventory.append(item)
    print(f"{item} was added to your inventory.")


def show_inventory():
    print("\nInventory")

    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print("-", item)


name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 12:
    print("You are a minor. The game is shutting down.")

else:
    print(f"Welcome, {name}!")

    number = random.randint(1, 10)

    while True:
        print("\nMain Menu")
        print("arvaa - Guess the number")
        print("vihje - Get a hint")
        print("uusi - Start a new game")
        print("lisaa - Add item to inventory")
        print("reppu - Show inventory")
        print("lopeta - Quit the game")

        command = input("Enter command: ")

        if command == "arvaa":
            guess_number(number)

        elif command == "vihje":
            get_hint(number)

        elif command == "uusi":
            number = new_game()

        elif command == "lisaa":
            add_item()

        elif command == "reppu":
            show_inventory()

        elif command == "lopeta":
            print("Game over. Goodbye!")
            break

        else:
            print("Unknown command.")