st = "PROGRAMMING"
st1 = ""
i = 0
j = 1
while j < len(st) and i < len(st):
    st1 += st[j]+st[i]
    i = i + 2
    j = j + 2

if len(st)%2 == 1:
    st1 += st[i]

print(st1)