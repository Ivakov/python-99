import sys
sys.path.append('../')

from P39.main import prime_numbers

def goldbach(x):
    for i in  prime_numbers(2,x):
        if x-i in prime_numbers(2,x):
            return [i,x-i]
    return []
