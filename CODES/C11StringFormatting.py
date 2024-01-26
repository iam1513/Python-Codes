# Can add numbers int0 string -> Fomatting
cost = 100

text = "This pen costs {}"
print(text.format(cost),"\n")

# Can mention index and include multiple data types
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))