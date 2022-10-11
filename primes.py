"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f'Number of primes must be 1 or higher.n/Number specified: {number_of_primes}')
    list = []
    n = 2
    prime = True
    while len(list) < number_of_primes:
        for i in range(2, n):
            if n % i == 0:
                prime = False
        if prime:
            list.append(n)
        n += 1
        prime = True

    return list
