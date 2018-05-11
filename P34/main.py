import sys
sys.path.append('../') 

from P33.main import is_coprime

def totient_phi(x):
    count = 0
    for y in range(1,x):
        if is_coprime(x,y):
            count = count + 1
    
    return count
