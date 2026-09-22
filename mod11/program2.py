'''class Car:
    def __init__(self, registration_number, speed):
        self.registration_number = registration_number
        self.speed = speed
    def print_information
class ElectricCar:
    def __init__(self, registration_number, speed, battery):
        
        self.battery = battery
        super().__init__(registration_number, speed)
class GasolineCar:
    def __init__(self, registration_number, speed, tank_volume):
        
        self.tank_volume = tank_volume
        super().__init__(registration_number, speed)
    def print_information(self):'''
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_capacity):
        super().__init__(registration_number, maximum_speed)
        self.tank_capacity = tank_capacity


# Main program
electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

# Select speeds
electric_car.current_speed = 120
gasoline_car.current_speed = 100

# Drive for three hours
electric_car.drive(3)
gasoline_car.drive(3)

# Print travelled distances
print("Electric car travelled distance:", electric_car.travelled_distance, "km")
print("Gasoline car travelled distance:", gasoline_car.travelled_distance, "km")
