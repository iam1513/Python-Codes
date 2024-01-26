# DATA MODELLING  > creating data models using the syntax and env of python 
#                > is composed of these objects > each entity is treated as an object > each entity has its own attributes and methods
#                1> Identity of an object - can never be changed once it is created - object address int the memory
# Data modelling - prim no prim   

a = "data"
print(id(a)) # id of the object will be printed (mem add)

b = "data"
print(id(b)) # same id as above as we passed the same string

print(a is b) # Checkig if they are same or not
print(id(a) is id(b)) 

#                2> Types of the Object - the object belong to which data type

a = 1001
print(type(a))

b = "om"
print(type(b))