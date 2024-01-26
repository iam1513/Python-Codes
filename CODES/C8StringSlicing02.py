# We can also either specify starting or just ending position leaving the opposite blank

word = "composition"

print()
print("Length of the word is : ",len(word))

# Specifying just end position
sl1 = word[:5]
# letters from index 0 to 4 will be printed, 0 will be default start location if nothing is specified
print("The sliced word without specifying the starting position is : ", sl1)

# Specifying just starting position
sl2 = word[5:]
# letters from index 5 to end will be printed, last index will be default end location if nothing is specified
print("The sliced word without specifying the ending position is : ", sl2)

# can also be sliced using negative indexing
sl3 = word[-5:-1]
# Starting postion is 5 from last, ending position is 1 from the end 
print("String sliced with negative index is : ", sl3)

# Point to be noted is , here the word from end will also be printed 
# Check in output, itio is your output and o is last second eithe -1 index word