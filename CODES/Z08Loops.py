# LOOPS - Iteration : > Repeat same work n number of times 

x = int(input("Enter the number of which you want factorial :"))

# Using for loop
fac = 1
print("\n Using for loop : ")
for i in range(1,x+1):

    fac = fac * i
print(fac)

# Using while loop
print("\n Using while loop : ")
fac = 1
i = 1
while(i<=x):
    fac = fac * i
    i += 1
print(fac)