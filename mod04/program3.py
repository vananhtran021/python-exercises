gender = input("Enter your gender (M/F): ")
hemoglobin_level = float(input("Enter your hemoglobin value (g/L): "))
if gender == "F" or gender == "f":
    if hemoglobin_level < 117:
        print("Your hemoglobin value is low.")
    elif hemoglobin_level < 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
elif gender == "M" or gender == "m":
    if hemoglobin_level < 134:
        print("Your hemoglobin value is low.")
    elif hemoglobin_level < 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
else:
    print("Invalid gender input.")