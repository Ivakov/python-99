import sys
sys.path.append('../') 

from P32.main import gcd

def totient_phi(x):
    a = []
    for y in range(1,x):
        if gcd(x,y) == 1:
            a.append(y)
    
    return len(a)
            
