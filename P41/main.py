import sys
sys.path.append('../')

from P40.main import goldbach

def goldbach_list(lower_limit,upper_limit,condition=0):
    ret = []
    for i in range(lower_limit,upper_limit+1):
        assign = goldbach(i)
        if assign:
            prime_sum = [i] + assign
            if condition == 0 or assign[0] > condition and assign[1] > condition:
                ret.append(prime_sum)
    return ret       
