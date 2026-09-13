airports = {}

while True:
    print("\nAirport Database")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        icao = input("Enter the ICAO code: ")
        name = input("Enter the airport name: ")

        airports[icao] = name
        print("Airport added.")

    elif choice == "2":
        icao = input("Enter the ICAO code: ")

        if icao in airports:
            print("Airport:", airports[icao])
        else:
            print("Airport not found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")