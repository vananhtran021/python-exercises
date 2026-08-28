dog1="A"
dog2="B"
if dog1==dog2:
    print("The dogs are the same")
    print(ord(dog1))
    print(ord(dog2))

age=int(input("Enter your age : "))
if 15<= age <18:
    weight=float(input("Enter your weight (kg): "))
if (age>=18 or age >=15 and weight >=55):
    print("The medicine can be used.")
else:
    print("The medicine cannot be used.")

age=int(input("Enter your age: "))
if age>=65:
    print("Your are retired.")
elif age>=18:
    print("You are an working-age.")   
elif age>=7:
    print("You are in school.")
elif age>=3:
    print("You are preschooler.")
else:
    print("You are a toddler.")

grade=int(input("Enter your grade: "))
if grade>=90:
    print("You got an A1.")
elif grade>=80:
    print("You got an A2.")
elif grade>=70:
    print("You got a B1.")
elif grade>=60:
    print("You got a B2.")
elif grade>=50:
    print("You got a C.")
else:
    print("You failed .")

status=input("Do you have a citizenship? (yes/no): ")
age=int(input("Enter your age: " ))
if status=="yes" and age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")