#1
'''days=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
day_number = int(input("Enter the day number (1-7): "))
day = days[day_number - 1]
print(f"Day number {day_number} is {day}.")

#print(days)
#print(type(days))
#2
students = ("Alice", "Bob", "Charlie", "David")
(student1, student2, student3, student4) = students
print(f"The students are: {student1}, {student2}, {student3}, and {student4}.")
#3
import random
def cast():
    first, second = random.randint(1, 6), random.randint(1, 6)
    return first, second
die1, die2 = cast()
print(f"The die showed {die1} and {die2}.")
#4

from tkinter.font import names


numbers = {"Viivi": "01-01-2000", "Olga": "05-12-1990"}
print(numbers)
names.add("Mary")
numbers["Olga"] = "05-12-1990"
numbers["Mary"] = "12-05-1995"
print(numbers)
name = input("Enter a name: ")
if name in numbers:
    print(f"{name}'s birthday is {numbers[name]}.")
else:
    print(f"{name} is not in the dictionary.")'''
#5
second_car = cars[1]
print("Information about the second car:")
print(second_car)
first_car = cars[0]["make"]
print(f"The first car's make is {first_car_make}.")






