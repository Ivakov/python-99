import sys
sys.path.append('../')

from P39.main import prime_numbers
from P31.main import is_prime

def goldbach(x):
    for i in  prime_numbers(2,x):
        if is_prime(x-i):
            return [i,x-i]
    return []             
