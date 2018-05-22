import sys
sys.path.append('../')

from P39.main import prime_numbers

def goldbach(x):
    if x % 2 != 0 or x <= 2:
        return []
    primes = prime_numbers(2,x)
    for i in primes:
        difference = x - i 
        if difference in primes:
            return [i,difference]
    return []
