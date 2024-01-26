str = "tenet"

i = 0
j = len(str) - 1

while(i <= j):
    if(str[i] != str[j]):
        print("Not Palindrome")
        break
    i = i + 1
    j = j - 1
else:
    print("Palindrome")
