import sys
sys.path.append('../')

from P31.main import is_prime

def prime_factors(x,ret=[]):
    for i in range(x+1):
        if is_prime(i):
            if x % i == 0:
                quotient = x // i
                add = ret + [i]
                return prime_factors(quotient,add)

    return ret          
