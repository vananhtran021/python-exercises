class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        # Speed cannot exceed maximum speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        # Speed cannot be less than zero
        if self.current_speed < 0:
            self.current_speed = 0


# Main program
car = Car("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print("Current speed:", car.current_speed, "km/h")

# Emergency brake
car.accelerate(-200)

print("Final speed:", car.current_speed, "km/h")