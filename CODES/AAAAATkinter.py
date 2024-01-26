import re
text = "Python is awesome!"
pattern = "^Python.*awesome!$"
result = re.match(pattern, text)

if result:
    print("Entire string matches.")
else:
    print("No match.")
