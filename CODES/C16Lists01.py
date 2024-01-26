# LISTS  :  > Mutable > Indexing start from 0 > Last index is -1 
#           > Expressed in [] > Can have multiple data types in singgle list

a = ['om' , 'harsh' , 2, 4]
print(a)

print("\nStarting element in the list is : ",a[0])
print("\nLast element in the list is : ",a[-1])

a.append(6) # Strings are mutable, We added 6 to our list

print("\nNew List is : ",a)
print("\nLength of updated list is : ", len(a))

