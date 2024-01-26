fruits = ["Apple", "Banana", "Guava", "Cherry"]

print("\n 1. ")
for x in fruits:
    print(x)
    if x=="Banana":
        break            # Apple and Banana will be printed as print is before checking if

print("\n 2. ")
for x in fruits:
    if x=="Banana":
        break
    print(x)             # Only Apple will be printed as print is after checking if