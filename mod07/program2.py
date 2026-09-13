import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    sides = int(input("How many sides does the dice have? "))

    while True:
        roll = roll_dice(sides)
        print(roll)

        if roll == sides:
            break

main()