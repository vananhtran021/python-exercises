correct_username = "exercise"
correct_password = "1234"

attempts = 0

while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break

    attempts += 1
    print("Incorrect username or password")

if attempts == 5:
    print("Access denied")





