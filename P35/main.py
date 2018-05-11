import sys
sys.path.append('../')

from P31.main import is_prime

def prime_factors(x,ret=[]):
    for i in range(int(x+1)):
        if is_prime(i):
            if x % i == 0:
                add = ret + ([i])
                j = x / i
                return prime_factors(j,add)

    return ret          
