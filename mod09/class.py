'''class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
dog1 = Dog("Buddy", "Golden Retriever")
print(f"Dog's Name: {dog1.name}, Breed: {dog1.breed}")
class Dog:
    def __init__(self, name, birth_year, sound="woof woof"):
        self.birth_year = birth_year
        self.name = name
        
        self.sound = sound
    def bark(self,times):
        for i in range(times):
            print(self.sound)
        return
dog1=Dog("Buddy", 2015)
dog2=Dog("Max", 2018, "waf waf")
print(f"Dog's Name: {dog1.name}, Birth Year: {dog1.birth_year}, Sound: {dog1.sound}")
print(f"Dog's Name: {dog2.name}, Birth Year: {dog2.birth_year}, Sound: {dog2.sound}")
dog1.bark(1)
dog2.bark(2)'''
class Dog:
    created = 0
    def __init__(self, name, birth_year, sound="woof woof"):
        self.birth_year = birth_year
        self.name = name
        self.sound = sound
        Dog.created += 1
dog1=Dog("Buddy", 2015)
dog2=Dog("Max", 2018, "waf waf")
dog3=Dog("Rocky", 2020, "arf arf")
print(f"Total dogs created: {Dog.created}")

