import sys
sys.path.append('../')

from P31.main import is_prime

def prime_factors(x):
    ret = []
    i = 2
    while i <= x:
        divide = divmod(x,i)
        if is_prime(i) and divide[1] == 0:
            ret.append(i)
            x = divide[0]
        else:
            i = i + 1
    return ret
