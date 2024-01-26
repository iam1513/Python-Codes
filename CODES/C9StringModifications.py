# Modifying all letters in the string to UPPER CASE
print("")
print("UPPER CASE MODIFICATION")
lan = "Python"
print(lan.upper())

# Modifying all letters in the string to lower case
print("")
print("lower CASE MODIFICATION")
lan = "PYTHON" # We modified value fron , Python to PYTHON, so now it is updated to PYTHON automatically
print(lan.lower())

# Removing White spaces -> The strip() method removes any whitespace from the beginning or the end
print("")
print("Strip MODIFICATION")
lan = "   Python Is A Programming Language    " # We modified value fron , Python to PYTHON, so now it is updated to PYTHON automatically
print(lan)
print(lan.strip())# Check this both outputs
# "Python Is A Programming Language" -> This will be our output

# Replacing -> The replace() method replaces a string with another string
print("")
print("REPLACING")
lan = "Python Is A Programming Language"
print(lan.replace("Python","Java"))

# Splitting -> The split() method returns a list where the text between the specified separator becomes the list items.
print("")
print("Splitting 01")
lan = "Python Is A Programming Language"
print(lan.split(" ")) # Whenever white space appears, the string will be splitted

print("")
print("Splitting 02")
lan = "PyGame"
print(lan.split("G")) 
# G wont be printed , before G will be splitted and after g will be splitted
# Output : ['Py', 'ame'] -> No G