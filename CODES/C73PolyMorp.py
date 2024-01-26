class Animal:
    def speak(self):
        pass  # This method will be overridden in the derived classes

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Function demonstrating polymorphism
def animal_sound(animal_instance):
    return animal_instance.speak()

# Create instances of different animals
dog = Dog()
cat = Cat()

# Use the function with different animal instances
print("Dog says:", animal_sound(dog))
print("Cat says:", animal_sound(cat))
