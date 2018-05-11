import sys
sys.path.append('../')

from P35.main import prime_factors

def prime_factors_multi(x):
    ret = []
    for i in  prime_factors(x):
        if (ret == [] or ret[-1][0] != i):
            ret.append([i,1])
        else:
            ret[-1][-1] = ret[-1][-1] + 1
 
    return ret
