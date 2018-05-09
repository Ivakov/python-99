import sys
sys.path.append('../')

from P32.main import gcd

def is_coprime(x,y):
    if gcd(x,y) == 1:
        return True
    else:
        return False
