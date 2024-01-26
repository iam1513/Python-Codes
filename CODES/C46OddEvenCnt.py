li = [1,3,4,12,7,2,34,20]

o_c = 0
e_c = 0

for i in li:
    if(i % 2 == 0):
        e_c = e_c + 1
    if(i % 2 == 1):
        o_c = o_c + 1

print(o_c)
print("\n",e_c)