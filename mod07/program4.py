def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def main():
    numbers = [5, 10, 15, 20]

    result = calculate_sum(numbers)

    print("The sum is:", result)


main()