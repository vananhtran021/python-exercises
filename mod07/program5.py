def remove_uneven(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    cut_down_list = remove_uneven(numbers)

    print("Original list:", numbers)
    print("Cut-down list:", cut_down_list)


main()