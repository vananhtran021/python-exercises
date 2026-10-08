# Mystery Room - Escape the House

## 1. Game Idea

Mystery Room is a command-line mystery adventure game.

The player wakes up inside a strange house and needs to
find a way to escape.

The player starts in the Bedroom and can choose between
three different escape routes.

The three routes are:

- Key -> Main Door -> END
- Book -> Puzzle Room -> END
- Coin -> Secret Passage -> END

Each route requires a different item.

The main goal of the game is:

**ESCAPE THE HOUSE.**

The game is designed for players aged 12+.

---

## 2. Objective

The player's objective is to:

1. Enter their name and age.
2. Start in the Bedroom.
3. Explore the available locations.
4. Find an important item.
5. Choose one of the three escape routes.
6. Use the correct item.
7. Escape the house.

There are three possible successful routes.

### Route 1 - Key

The player collects the Key and travels to the
Main Door.

The Key unlocks the door.

**Key -> Main Door -> END**

### Route 2 - Book

The player collects the Book and travels to the
Puzzle Room.

The Book helps the player solve the puzzle.

**Book -> Puzzle Room -> END**

### Route 3 - Coin

The player collects the Coin and travels to the
Secret Passage.

The Coin activates the hidden exit.

**Coin -> Secret Passage -> END**

All three routes allow the player to escape the house.

---

## 3. How the Game Works

The game uses a main menu.

The player can choose actions such as:

- Show current room
- Move
- Collect an item
- Show inventory
- Show player status
- Show all rooms
- Play the number guessing game
- Try to escape
- Save the game
- Show instructions
- Quit

The game continues until:

- The player successfully escapes, or
- The player chooses to quit.

---

## 4. Rooms

The game contains four main locations.

### Bedroom

This is the starting location.

The player begins the game here.

The Bedroom is the starting point for all three routes.

### Main Door

The Main Door is the exit for the Key route.

The player needs the Key to escape through it.

### Puzzle Room

The Puzzle Room is the exit for the Book route.

The player needs the Book to complete this route.

### Secret Passage

The Secret Passage is the exit for the Coin route.

The player needs the Coin to activate the exit.

---

## 5. Items

The game contains three important items:

- Key
- Book
- Coin

The items are stored in the player's inventory after
they are collected.

The inventory can also calculate how many items the player
has collected.

For example:

```text
========== INVENTORY ==========
- Key x1
- Coin x1

Total items: 2
===============================
````

---

## 6. Number Guessing Game

The game also contains a small number guessing game.

The computer generates a random number between 1 and 10.

The player has three attempts.

The player can also ask for a hint.

The hint tells the player whether the number is even or odd.

If the player guesses correctly:

**+10 points**

This is an additional feature that makes the game more
interactive.

---

## 7. Scoring System

The player can earn points during the game.

### Collecting an item

Each collected item gives:

**+5 points**

### Winning the number guessing game

A correct answer gives:

**+10 points**

The player's final score is shown when they escape.

---

## 8. Age Requirement

The game is rated 12+.

At the beginning of the game, the player enters their age.

If the player is under 12, the game stops.

This creates an age restriction as required by the game design.

---

## 9. Classes and Objects

The game uses object-oriented programming.

### Item

The `Item` class represents an item in the game.

Example:

```python
Item("Key")
Item("Book")
Item("Coin")
```

### Room

The `Room` class represents a location.

Each room has:

* A name
* A description
* An item
* Connections to other rooms

### Player

The `Player` class represents the person playing the game.

The player has:

* Name
* Age
* Current location
* Inventory
* Score

The Player class also contains functions for:

* Moving
* Collecting items
* Counting items
* Showing inventory
* Checking for items
* Showing player status

---

## 10. Functions

The project uses multiple functions to separate the game
into smaller parts.

Important functions include:

* `read_file()`
* `save_game()`
* `create_items()`
* `create_rooms()`
* `number_guessing_game()`
* `get_hint()`
* `show_current_room()`
* `move_player()`
* `check_escape_route()`
* `show_key_ending()`
* `show_book_ending()`
* `show_coin_ending()`
* `show_all_rooms()`
* `show_menu()`
* `show_instructions()`
* `create_player()`
* `handle_command()`
* `main()`

The functions make the code easier to understand,
test and maintain.

---

## 11. Lists

The game uses lists for several purposes.

The player's inventory is a list:

```python
self.inventory = []
```

When the player collects an item, it is added to the list.

The list can then be used to:

* Store collected items
* Count items
* Check whether an item exists
* Display the inventory

Room connections are also stored in a list.

---

## 12. File Handling

The game uses files to store and read information.

### intro.txt

Contains the introduction and story setup.

### instructions.txt

Contains the game instructions.

### savegame.txt

Stores player information when the player chooses
the Save Game option.

The program uses Python file handling with:

```python
open()
```

and:

```python
with open(...)
```

---

## 13. Project Structure

The project can be organised like this:

```text
MysteryRoom/
│
├── main.py
├── intro.txt
├── instructions.txt
├── savegame.txt
├── README.md
│
└── game/
    ├── __init__.py
    ├── item.py
    ├── room.py
    └── player.py
```

---

## 14. How to Run

Open the project folder in a terminal.

Run:

```bash
python main.py
```

The game will start by displaying the introduction.

The player must enter:

* Name
* Age

Players under 12 cannot continue.

---

## 15. Three Routes

The main game structure is:

```text
                    START
                      |
                   Bedroom
                  /    |    \
                 /     |     \
              Key     Book    Coin
               |       |       |
          Main Door  Puzzle  Secret Passage
               |       |       |
              END     END     END
```

The three routes give the player different ways to
complete the game.

This means the game can be completed in at least
three different ways.

---

## 16. SDG Connection

The game is mainly focused on mystery, exploration and
problem solving.

It can also be connected to **UN Sustainable Development
Goal 12: Responsible Consumption and Production** in a
small way.

The game encourages the player to:

* Collect only useful objects.
* Pay attention to what objects are needed.
* Think carefully before using or collecting items.
* Understand that objects can have different purposes.

The SDG connection is secondary to the main mystery
and escape story.

---

## 17. Programming Concepts Used

This project demonstrates several Python programming
concepts:

* Variables
* Input and output
* `if` statements
* `while` loops
* `for` loops
* Functions
* Parameters
* Return values
* Lists
* Classes
* Objects
* File reading
* File writing
* Random numbers
* String handling
* Error handling
* Object-oriented programming

---

## 18. Extra Features

Additional features included in the game are:

* Number guessing mini-game
* Hint system
* Scoring system
* Inventory item counting
* Multiple escape routes
* Age restriction
* Save game functionality
* Separate game classes
* Three different ending messages

---

## 19. Conclusion

Mystery Room is a simple command-line adventure game
where the player must escape a mysterious house.

The player starts in the Bedroom and must find one of
three important objects:

**Key, Book or Coin**

Each object leads to a different escape route.

The three possible endings are:

**Key -> Main Door -> Escape**

**Book -> Puzzle Room -> Escape**

**Coin -> Secret Passage -> Escape**

The main purpose of the project is to demonstrate
Python programming concepts through an interactive game.
