#1
length = float(input("Enter the length of the zander in centimeters: "))

if length < 42:
    difference = 42 - length
    print("Release the fish back into the lake.")
    print(f"The fish was {difference:.1f} cm below the size limit.")
else:
    print("The fish meets the size limit.")