import sys
sys.path.append('../') 

from P33.main import is_coprime

def totient_phi(x):
    a = []
    for y in range(1,x):
        if is_coprime(x,y):
            a.append(y)

    return len(a)
