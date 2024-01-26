# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1] # Reverse string


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
