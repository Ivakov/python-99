import sys
sys.path.append('../')

from P40.main import goldbach

def goldbach_list(lower_limit,upper_limit,condition=0):
    ret = []
    for i in range(lower_limit,upper_limit+1):
        assign = goldbach(i)
        if assign and assign[0] > condition:
            ret.append([i]+assign)
    return ret       
