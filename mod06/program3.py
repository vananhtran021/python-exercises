number = int(input("Enter an integer: "))

is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print("The number is a prime number.")
else:
    print("The number is not a prime number.")