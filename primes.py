"""Prime number functions."""


def is_prime(num):
    """Check if an integer is prime."""
    if num == 0 or abs(num) == 1:
        return False
    for i in range(2, abs(num)):
        if num % i == 0:
            return False
    return True


def get_primes(s, e):
    """Return list of prime numbers in given range."""
    primes = list()
    for i in range(s, e + 1):
        if is_prime(i):
            primes.append(i)
    return primes


print get_primes(1, 100)
