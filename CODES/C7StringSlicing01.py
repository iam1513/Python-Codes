# using len function, we can also find  length of our string

question = "What are you doing?"
x = len(question)

# Total letters in question are :
print()
print("Total letters in the string are : ",x)
print()

# We can slice the  string
# For example , we need the word are from the above string , we can slice string from index 4 - 8
# The character are index 4 will be included in the string but the one at index 8 wont

sl = question[4:8]

print("The sliced part of string is '",sl,"'")

# Check the output, are must have been printed for sure ...
# You might be having trouble removing the space before a
# That is because , we have space at index 4
# Try for 5-8

sl1 = question[5:8]

print("The sliced part of string is '",sl1,"'")
