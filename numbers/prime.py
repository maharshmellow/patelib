def isPrime(n):
    """Checks if the number n is a prime number"""
    if n % 2 == 0 and n > 2:
        return False

    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
