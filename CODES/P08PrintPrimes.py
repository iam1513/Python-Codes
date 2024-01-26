def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_n_primes(n):
    """Print the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1

    print(f"The first {n} prime numbers are: {primes}")

# Get user input for the number of prime numbers to print
n = int(input("Enter the value of n: "))

# Call the function to print the first n prime numbers
print_n_primes(n)