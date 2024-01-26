def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)

num1, num2 = 36, 48
gcd = find_gcd(num1, num2)
lcm = find_lcm(num1, num2)

print(f"GCD of {num1} and {num2}: {gcd}")
print(f"LCM of {num1} and {num2}: {lcm}")
