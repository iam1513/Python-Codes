# INHERITENCE : > inherited from parent to child 
class State:
    def location(self):
        print("Located in India")

class Maharshtra(State):
    def capital(self):
        print("Capital of Maharastra is Mumbai")

    def direction(self):
        print("State in West of India.")

class Gujrat(Maharshtra): # Cat inherits properties from Dog as well as Animal as Dog inherit properties from animal 
    def capital(self):
        print("Capital of Gujrat is Gandhinagar.")   

    def speciality(self):
        print("Speciality of Gujrat is its amazing culture and delicious food.") 

       
print("\n")
maha = Maharshtra()
maha.capital() # Can access from Animal Super class though we dont have speak in Dog class
maha.location()
maha.direction()
print("\n")
guj = Gujrat()
guj.capital()
guj.speciality()


# MULTI LEVEL INHERITENCE : > Some properties of parent class is derived at each level(inheritence from previous level) 
#                           > no limit for number of levels

# MULTIPLE INHERITENCE      > issubclass(derived,parent) ---> to check if derived class is sub-class of parent or not
# class a:
#     ....

# class b:
#     ....

# class c(a,b): Inherits from both above classes 
#     ....
    