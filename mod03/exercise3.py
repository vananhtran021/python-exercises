#1
name=input("Please enter your name: ")
print("Hello, " + name + "!")
#2
import math
rad=float(input("Please enter the radius of the circle: "))
area=math.pi*rad*rad
print(f"The area of the circle is: {area:10.3f}")
#3
length=float(input("Please enter the length of the rectangle: "))
width=float(input("Please enter the width of the rectangle: "))
perimeter_rectangle=2*(length+width)
print(f"The perimeter of the rectangle is: {perimeter_rectangle:10.3f}")
area_rectangle=length*width
print(f"The area of the rectangle is: {area_rectangle:10.3f}")
#4
num1=int(input("Please enter number 1: "))
num2=int(input("Please enter number 2: "))
num3=int(input("Please enter number 3: "))
sum=num1+num2+num3
print("The sum of the three numbers is: " + str(sum))
product=num1*num2*num3
print("The product of the three numbers is: " + str(product))
avg=(num1+num2+num3)/3
print("The average of the three numbers is: " + str(avg))

#5
talents = float(input("Please enter talents:\n"))
pounds = float(input("Please enter pounds:\n"))
lots = float(input("Please enter lots:\n"))

total_lots = talents * 20 * 32 + pounds * 32 + lots

total_grams = total_lots * 13.3

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")

#11
import random

# 3-digit code: each number is between 0 and 9
code_3 = ""

for i in range(3):
    code_3 += str(random.randint(0, 9))

# 4-digit code: each number is between 1 and 6
code_4 = ""

for i in range(4):
    code_4 += str(random.randint(1, 6))

print("3-digit code:", code_3)
print("4-digit code:", code_4)



