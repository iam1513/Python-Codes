# MULTIPLE INHERITANCE
class Animal:
    def speak(self):
        print("Animal Speaking")

class Canine:
    def legs(self):
        print("Have 4 legs")

class Dog(Animal, Canine):  # Dog inherits properties from both Animal and Canine
    def bark(self):
        print("Dog is barking")

class Cat(Dog):  # Cat inherits properties from Dog, which in turn inherits from Animal and Canine
    def meow(self):
        print("Cat is making sound")

# Create instances
d = Dog()
c = Cat()

# Accessing methods from multiple inheritance
d.speak()  # Access method from 'Animal' class
d.legs()   # Access method from 'Canine' class
d.bark()

c.legs()   # Access method from 'Canine' class
c.meow()
