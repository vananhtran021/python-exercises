import random

name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 12:
    print("You are a minor. The game is shutting down.")

else:
    print(f"Welcome, {name}!")

    number = random.randint(1, 10)

    while True:
        print("\n--- Main Menu ---")
        print("arvaa - Guess the number")
        print("vihje - Get a hint")
        print("uusi - Start a new game")
        print("lopeta - Quit the game")

        command = input("Enter command: ")

        if command == "arvaa":
            guess = int(input("Guess a number from 1 to 10: "))

            if guess == number:
                print("Correct! You guessed the number!")
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")

        elif command == "vihje":
            print("The number is between 1 and 10.")

        elif command == "uusi":
            number = random.randint(1, 10)
            print("A new number has been chosen!")

        elif command == "lopeta":
            print("Game over. Goodbye!")
            break

        else:
            print("Unknown command.")