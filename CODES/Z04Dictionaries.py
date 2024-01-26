# Dictionaries : > Key : Value pairs > Ordered > Mutable > does not allow duplicates > Reperesented by {}

di= {
    # Don't forget : , Don't use =
    "name" : "Om",
    "age" : 19, # Key and value can be of different data types and key can also be of int, str, etc .., not necessarily str 
    "from" : "Maharashtra"
}
di["name"] = "Rahul" # Can update values
print("\n",di)

# Getting value of the key
print("\nThe value stored in key 'name' is :",di["name"])

# Deletion in Dictionary
del di["name"]

print("\n",di) # "name" key and its value will be deleted 

# If we to only print keys
print("\nThe keys are : ",di.keys())
print("\n",list(di.keys()))

# If we to only print values
print("\nThe values are : ",di.values())
print("\n",list(di.values()))