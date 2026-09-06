name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 12:
    print("You are a minor. The game is shutting down.")

else:
    print(f"Welcome, {name}!")

    while True:
        print("\n--- Main Menu ---")
        print("tervehdys - Say hello")
        print("taistelu - Fight a monster")
        print("aarre - Find a treasure")
        print("lopeta - Quit the game")

        command = input("Enter command: ")

        if command == "tervehdys":
            print("The wizard says: Hello, brave adventurer!")

        elif command == "taistelu":
            print("You fight a dragon and win!")

        elif command == "aarre":
            print("You found a treasure chest!")

        elif command == "lopeta":
            print("Game over. Goodbye!")
            break

        else:
            print("Unknown command.")