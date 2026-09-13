import math

def unit_price(diameter, price):
    radius = diameter / 2
    area_cm2 = math.pi * radius ** 2
    area_m2 = area_cm2 / 10000

    return price / area_m2


def main():
    diameter1 = float(input("Enter the diameter of pizza 1 (cm): "))
    price1 = float(input("Enter the price of pizza 1 (€): "))

    diameter2 = float(input("Enter the diameter of pizza 2 (cm): "))
    price2 = float(input("Enter the price of pizza 2 (€): "))

    unit_price1 = unit_price(diameter1, price1)
    unit_price2 = unit_price(diameter2, price2)

    print(f"Pizza 1 unit price: {unit_price1:.2f} €/m²")
    print(f"Pizza 2 unit price: {unit_price2:.2f} €/m²")

    if unit_price1 < unit_price2:
        print("Pizza 1 provides better value for money.")
    elif unit_price2 < unit_price1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")


main()