def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1, num2 = 36, 48
gcd = find_gcd(num1, num2)
print(f"GCD of {num1} and {num2}: {gcd}")
