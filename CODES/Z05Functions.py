# FUNCTIONS : > block of code only runs when it is called > can pass values , known as parameters > return data as result
#             > Creating using def 

# Creating a function
def fun_1():
    print("\nThis is my first Function")

# Calling a functino
fun_1() 

# Information can be passed into functions as arguments
def fun_2(fname): # fname -> parameter
    print(fname + " student")

fun_2("\nGood") # Arguments
fun_2("Better")
fun_2("Best")

# Multiple items are passed by ref
