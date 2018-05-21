import sys
sys.path.append('../')

from P31.main import is_prime

def prime_factors(x):
    ret = []
    for i in range(x+1):
        if is_prime(i):
            divide = divmod(x,i)
            if divide[1] == 0:
                ret.append(i)
                while divide[0] % i == 0:
                    ret.append(i) 
                    divide = (divide[0] // i, None)
    return ret
