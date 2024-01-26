li = [2,4,1,6,8,2]

x = li[0]

for i in range(0,len(li)):
    if(x<li[i]):
        x = li[i]

print(x)