
def fibo_ser(n):
    a,b = 0 , 1
    count = 0
    
    while(count<n) :
        print(a)
        a,b = b, a+b
        count+=1
        
fibo_ser(4)