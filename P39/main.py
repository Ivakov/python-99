import sys
sys.path.append('../')

from P31.main import is_prime

def prime_numbers(x,y):
    if x > y:
        x,y = y,x
    
    primes = []
    for i in range(x,y+1):
        if is_prime(i):
            primes.append(i)

    return primes
    
