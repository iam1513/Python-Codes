# FILE OPERATIONS : > Opening a file > A file operation starts with the open() fun in py 
#                   > accepts 2 arg, file name and access mode int which file can be accesed
#                   > 

fileptr = open("CODES/file.txt","r")

if fileptr:
    print("File opened successfully")
else:
    print("File not present")

fileptr = open("CODES/file.txt","w")
fileptr.write("I am Om , the zhingur.")
fileptr = open("CODES/file.txt")
content = fileptr.read()
print(type(content))
print(content)