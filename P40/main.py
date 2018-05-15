import sys
sys.path.append('../')

from P39.main import prime_numbers

def goldbach(x):
    y = 0
    for i in prime_numbers(y,x):
        for j in prime_numbers(i,x):
            if i + j == x:
                return [i,j]
    return []
            
