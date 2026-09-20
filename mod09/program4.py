import random


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


# Create 10 cars
cars = []

for i in range(1, 11):
    maximum_speed = random.randint(100, 200)
    registration_number = f"ABC-{i}"

    car = Car(registration_number, maximum_speed)
    cars.append(car)


# Race
while True:
    for car in cars:
        # Change speed randomly between -10 and +15 km/h
        change = random.randint(-10, 15)
        car.accelerate(change)

        # Drive for one hour
        car.drive(1)

    # Check if any car has travelled at least 10,000 km
    if any(car.travelled_distance >= 10000 for car in cars):
        break


# Print results
print(f"{'Registration':<15}{'Max speed':<15}"
      f"{'Current speed':<15}{'Distance':<15}")

for car in cars:
    print(f"{car.registration_number:<15}"
          f"{car.maximum_speed:<15}"
          f"{car.current_speed:<15}"
          f"{car.travelled_distance:<15.1f}")