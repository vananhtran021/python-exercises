import random

dice = int(input("How many dice do you want to roll? "))

sum = 0

for i in range(dice):
    roll = random.randint(1, 6)
    sum += roll

print("The sum of the dice is:", sum)
