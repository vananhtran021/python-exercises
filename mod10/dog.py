class Dog:
    def __init__(self, name, birth_year, sound="woof woof"):
        self.birth_year = birth_year
        self.name = name
        self.sound = sound
    def bark(self, times):
        for i in range(times):
            print(self.name + "bark: " +self.sound)
        return
    
from dog import Dog   
class Hotel:
    def __init__(self):
        self.dogs=[]
    def dog_checkin(self, dog):
        self.dog.append(dog)
        print(dog.name +" checked in ")
    def dog_checkout(self, dog):
        self.dogs.remove(dog)
        print(dog.name + " checked out ")
    def greet_dogs (self):
        for dog in self.dogs:
            dog.bark(1)

#main
dog1=Dog("Buddy", 2015)
dog2=Dog("Max", 2018, "waf waf")
hotel=Hotel()
hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.greet_dogs()
hotel.dog_checkout(dog1)
hotel.greet_dogs()
