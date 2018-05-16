import sys
sys.path.append('../')

from P39.main import prime_numbers

def goldbach(x):
    primes = prime_numbers(2,x)
    for i in  primes:
        for j in primes:
            if i + j == x:
                return [i,j]
    return []             
