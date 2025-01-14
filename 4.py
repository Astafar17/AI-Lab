# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to get all prime numbers in a range
def display_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Display prime numbers from 1 to 100
primes = display_primes_in_range(1, 100)
print("Prime numbers from 1 to 100 are:")
print(primes)
