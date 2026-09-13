def gallons_to_litres(gallons):
    return gallons * 3.78541


def main():
    while True:
        gallons = float(input("Enter gallons: "))

        if gallons < 0:
            break

        litres = gallons_to_litres(gallons)
        print(f"{litres:.2f} litres")


main()