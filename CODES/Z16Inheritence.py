# INHERITENCE : > inherited from parent to child 
class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

    def legs(self):
        print("Have 4 legs")

class Cat(Dog): # Cat inherits properties from Dog as well as Animal as Dog inherit properties from animal 
    def meow(self):
        print("Cat is making sound")       

d = Dog()

d.speak() # Can access from Animal Super class though we dont have speak in Dog class
d.bark()

c = Cat()
c.legs()
c.meow()

# MULTI LEVEL INHERITENCE : > Some properties of parent class is derived at each level(inheritence from previous level) 
#                           > no limit for number of levels

# MULTIPLE INHERITENCE      > issubclass(derived,parent) ---> to check if derived class is sub-class of parent or not
# class a:
#     ....

# class b:
#     ....

# class c(a,b): Inherits from both above classes 
#     ....
    