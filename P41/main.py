import sys
sys.path.append('../')

from P40.main import goldbach

def goldbach_list(x,y,z=None):
    ret = []
    for i in range(x,y+1):
        assign = goldbach(i)
        if assign:
            prime_sum = [i] + assign
            if (z == None or assign[0] > z and assign[1] > z):
                ret.append(prime_sum)
    return ret 
