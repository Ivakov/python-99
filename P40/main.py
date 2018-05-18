import sys
sys.path.append('../')

from P39.main import prime_numbers

def goldbach(x):
    primes = prime_numbers(2,x)
    for i in primes:
        difference = x-i 
        if difference in primes and x % 2 == 0:
            return [i,difference]
    return []
