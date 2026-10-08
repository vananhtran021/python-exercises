import random

from game.item import Item
from game.room import Room
from game.player import Player


# ==========================================
# FILE FUNCTIONS
# ==========================================

def read_file(filename):
    """Read and return text from a file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""


def save_game(player):
    """Save the player's progress to a file."""
    with open("savegame.txt", "w", encoding="utf-8") as file:
        file.write(f"{player.name}\n")
        file.write(f"{player.age}\n")
        file.write(f"{player.location.name}\n")
        file.write(f"{player.score}\n")

        item_names = []

        for item in player.inventory:
            item_names.append(item.name)

        file.write(",".join(item_names))

    print("\nGame saved successfully!")


# ==========================================
# CREATE ITEMS
# ==========================================

def create_items():
    """Create the items used in the game."""
    return {
        "Key": Item("Key"),
        "Book": Item("Book"),
        "Coin": Item("Coin")
    }


# ==========================================
# CREATE ROOMS
# ==========================================

def create_rooms(items):
    """
    Create the rooms and connect them.

    The player starts in the Bedroom.

    There are three escape routes:

    Key  -> Main Door
    Book -> Puzzle
    Coin -> Secret Passage
    """

    bedroom = Room(
        "Bedroom",
        "You wake up in a strange bedroom. "
        "You are trapped inside a mysterious house. "
        "Three objects may help you escape."
    )

    main_door = Room(
        "Main Door",
        "A large locked door stands in front of you. "
        "There is a keyhole on the door."
    )

    puzzle = Room(
        "Puzzle Room",
        "You enter a strange room filled with symbols. "
        "A mysterious book may contain the answer."
    )

    secret_passage = Room(
        "Secret Passage",
        "You discover a hidden passage behind the wall. "
        "A strange coin seems to activate the exit."
    )

    # The three important items start in the Bedroom.
    bedroom.item = items["Key"]

    # Store the other route objects in their destination rooms.
    main_door.item = None
    puzzle.item = items["Book"]
    secret_passage.item = items["Coin"]

    # Three routes from Bedroom.
    bedroom.add_connection(main_door)
    bedroom.add_connection(puzzle)
    bedroom.add_connection(secret_passage)

    return [bedroom, main_door, puzzle, secret_passage]


# ==========================================
# NUMBER GUESSING GAME
# ==========================================

def number_guessing_game(player):
    """Play a small number guessing challenge."""

    secret_number = random.randint(1, 10)
    attempts = 3

    print("\n========== NUMBER GUESSING ==========")
    print("Guess a number between 1 and 10.")
    print("You have 3 attempts.")
    print("You can type 'hint' for a clue.")

    for attempt in range(1, attempts + 1):

        guess = input(f"\nAttempt {attempt}: ").strip()

        if guess.lower() == "hint":
            get_hint(secret_number)
            continue

        if not guess.isdigit():
            print("Please enter a number.")
            continue

        guess = int(guess)

        if guess == secret_number:
            print("\nCorrect!")
            print("You earned 10 points!")
            player.score += 10
            return True

        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

    print(f"\nThe correct number was {secret_number}.")
    return False


def get_hint(secret_number):
    """Give the player a hint."""
    if secret_number % 2 == 0:
        print("Hint: The number is even.")
    else:
        print("Hint: The number is odd.")


# ==========================================
# MOVEMENT
# ==========================================

def show_current_room(player):
    """Show the player's current room."""
    player.location.show_room()


def move_player(player):
    """Allow the player to move to another connected room."""
    connections = player.location.connections

    if not connections:
        print("\nThere are no exits from this room.")
        return

    print("\nWhere do you want to go?")

    for number, room in enumerate(connections, start=1):
        print(f"{number}. {room.name}")

    choice = input("\nChoose a room: ").strip()

    if not choice.isdigit():
        print("Please enter a number.")
        return

    choice = int(choice)

    if 1 <= choice <= len(connections):
        player.move(connections[choice - 1])
    else:
        print("Invalid choice.")


# ==========================================
# ROUTE CHECKING
# ==========================================

def check_escape_route(player):
    """
    Check which escape route the player has chosen.

    Key  -> Main Door
    Book -> Puzzle
    Coin -> Secret Passage
    """

    if player.location.name == "Main Door":
        if player.has_item("Key"):
            show_key_ending(player)
            return True

        print("\nThe Main Door is locked.")
        print("You need the Key.")
        return False

    if player.location.name == "Puzzle Room":
        if player.has_item("Book"):
            show_book_ending(player)
            return True

        print("\nThe puzzle cannot be solved.")
        print("You need the Book.")
        return False

    if player.location.name == "Secret Passage":
        if player.has_item("Coin"):
            show_coin_ending(player)
            return True

        print("\nThe secret passage is inactive.")
        print("You need the Coin.")
        return False

    return False


# ==========================================
# THREE ENDINGS
# ==========================================

def show_key_ending(player):
    """Ending for the Key route."""
    print("\n")
    print("======================================")
    print("          KEY ROUTE - END")
    print("======================================")
    print("You insert the Key into the Main Door.")
    print("The lock clicks open.")
    print("The door slowly opens.")
    print()
    print("You escaped the house!")
    print()
    print(f"Congratulations, {player.name}!")
    print(f"Final score: {player.score}")
    print("======================================")


def show_book_ending(player):
    """Ending for the Book route."""
    print("\n")
    print("======================================")
    print("          BOOK ROUTE - END")
    print("======================================")
    print("You open the mysterious Book.")
    print("Inside, you find the solution to the puzzle.")
    print("You enter the correct answer.")
    print("A hidden door opens.")
    print()
    print("You escaped the house!")
    print()
    print(f"Congratulations, {player.name}!")
    print(f"Final score: {player.score}")
    print("======================================")


def show_coin_ending(player):
    """Ending for the Coin route."""
    print("\n")
    print("======================================")
    print("          COIN ROUTE - END")
    print("======================================")
    print("You place the Coin into a strange slot.")
    print("The wall moves and reveals a secret passage.")
    print("You follow the passage outside.")
    print()
    print("You escaped the house!")
    print()
    print(f"Congratulations, {player.name}!")
    print(f"Final score: {player.score}")
    print("======================================")


# ==========================================
# ROOM INFORMATION
# ==========================================

def show_all_rooms(rooms):
    """Show all rooms in the game."""
    print("\n========== ROOMS ==========")

    for room in rooms:
        print(f"- {room.name}")

    print("===========================")


# ==========================================
# MENU
# ==========================================

def show_menu():
    """Display the main menu."""
    print("\n========== MYSTERY ROOM ==========")
    print("1. Show current room")
    print("2. Move")
    print("3. Collect item")
    print("4. Show inventory")
    print("5. Show player status")
    print("6. Show all rooms")
    print("7. Play number guessing game")
    print("8. Try to escape")
    print("9. Save game")
    print("10. Show instructions")
    print("11. Quit")
    print("==================================")


# ==========================================
# INSTRUCTIONS
# ==========================================

def show_instructions():
    """Display game instructions."""
    print("\n========== INSTRUCTIONS ==========")
    print("Your objective is to escape the house.")
    print()
    print("You start in the Bedroom.")
    print()
    print("There are three possible escape routes:")
    print("1. Key  -> Main Door")
    print("2. Book -> Puzzle Room")
    print("3. Coin -> Secret Passage")
    print()
    print("Explore the house.")
    print("Collect an item.")
    print("Choose a route.")
    print("Use the correct item to escape.")
    print()
    print("You can also play the number guessing game")
    print("to earn extra points.")
    print("==================================")


# ==========================================
# PLAYER CREATION
# ==========================================

def create_player(starting_room):
    """Create a player using their name and age."""

    print("\n========== PLAYER SETUP ==========")

    name = input("Enter your name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    while True:
        age_input = input("Enter your age: ").strip()

        if not age_input.isdigit():
            print("Please enter a valid age.")
            continue

        age = int(age_input)

        if age < 12:
            print("\nSorry, this game is rated 12+.")
            print("You cannot play this game.")
            return None

        break

    print(f"\nWelcome, {name}!")

    return Player(name, age, starting_room)


# ==========================================
# MAIN GAME LOOP
# ==========================================

def handle_command(choice, player, rooms):
    """
    Handle one menu choice.

    Returns True if the game should continue.
    Returns False when the game ends.
    """

    if choice == "1":
        show_current_room(player)

    elif choice == "2":
        move_player(player)

    elif choice == "3":
        player.collect_item()

    elif choice == "4":
        player.show_inventory()

    elif choice == "5":
        player.show_status()

    elif choice == "6":
        show_all_rooms(rooms)

    elif choice == "7":
        number_guessing_game(player)

    elif choice == "8":
        escaped = check_escape_route(player)

        if escaped:
            return False

    elif choice == "9":
        save_game(player)

    elif choice == "10":
        show_instructions()

    elif choice == "11":
        print("\nThanks for playing Mystery Room!")
        return False

    else:
        print("\nInvalid choice. Please choose 1-11.")

    return True


def main():
    """Start and run the Mystery Room game."""

    print(read_file("intro.txt"))

    items = create_items()
    rooms = create_rooms(items)

    starting_room = rooms[0]

    player = create_player(starting_room)

    if player is None:
        return

    show_instructions()

    game_running = True

    while game_running:
        show_menu()

        choice = input("\nChoose an option: ").strip()

        game_running = handle_command(
            choice,
            player,
            rooms
        )


if __name__ == "__main__":
    main()