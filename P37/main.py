import sys
sys.path.append('../')

from P36.main import prime_factors_multi

def totient_phi(x):
    assign = prime_factors_multi(x)
    assigned = 1
    for i in assign:
        expand = (i[0]-1) * i[0] ** (i[1]-1)
        assigned = assigned * expand

    return assigned

            
