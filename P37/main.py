import sys
sys.path.append('../')

from P36.main import prime_factors_multi

def totient_phi(x):
    assigned = prime_factors_multi(x)
    factor = []
    for i in assigned:
        multi = (i[0]-1) * i[0] ** (i[1]-1)
        if factor == []:
            factor.append(multi)
        else:
            factor = [factor[0] * multi]
          
    return factor[0]
            
