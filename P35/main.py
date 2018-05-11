import sys
sys.path.append('../')

from P31.main import is_prime

def prime_factors(x,ret=[]):
    for i in range(x+1):
        if is_prime(i):
            answer = divmod(x,i)
            if answer[1] == 0:
                add = ret + [i]
                return prime_factors(answer[0],add)

    return ret          
