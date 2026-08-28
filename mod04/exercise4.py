#1
length = float(input("Enter the length of the zander in centimeters: "))

if length < 42:
    difference = 42 - length
    print("Release the fish back into the lake.")
    print(f"The fish was {difference:.1f} cm below the size limit.")
else:
    print("The fish meets the size limit.")
#2
cabin_class = input("Enter the cabin class: ")

if cabin_class == "LUX":
    print("upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("windowless cabin above the car deck.")
elif cabin_class == "C":
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
#3
gender = input("Enter your gender (M/F): ")
hemoglobin_level = float(input("Enter your hemoglobin level (g/L): "))
if gender == "F":
    if hemoglobin_level < 117:
        print("Your hemoglobin level is low.")
    elif hemoglobin_level < 155:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
elif gender == "M":
    if hemoglobin_level < 134:
        print("Your hemoglobin level is low.")
    elif hemoglobin_level < 167:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
else:
    print("Invalid gender input.")
#4
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("The year is a leap year.")
elif year % 100 == 0:
    print("The year is not a leap year.")
elif year % 4 == 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")