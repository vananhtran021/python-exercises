def average_grade(grades):
    averages = []

    for grade_list in grades:
        average = sum(grade_list) / len(grade_list)
        averages.append(average)

    return averages


def main():
    grades = [
        [80.0, 90.0, 85.0],
        [70.0, 75.0, 80.0],
        [95.0, 90.0, 100.0]
    ]

    averages = average_grade(grades)

    for average in averages:
        print(f"{average:.2f}")

    main()

