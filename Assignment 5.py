class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("Running 🐕")

class Bird(Animal):
    def move(self):
        print("Flying 🦅")

class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Create instances of animals and vehicles
dog = Dog()
bird = Bird()
fish = Fish()

car = Car()
plane = Plane()
boat = Boat()

# List of all objects
objects = [dog, bird, fish, car, plane, boat]

# Call the move() method on each object
for obj in objects:
    obj.move()
