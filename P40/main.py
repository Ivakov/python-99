import sys
sys.path.append('../')

from P39.main import prime_numbers

def goldbach(x,y=0):
    for i in prime_numbers(x,y):
        for j in prime_numbers(x,y):
            if i + j == x:
                return [i,j]
    return []
