import sys
sys.path.append('../')

from P10.main import encode
from P35.main import prime_factors

def prime_factors_multi(x):
    assigned = prime_factors(x)
    encoded = encode(assigned)
    for e in encoded:
        e.reverse()

    return encoded
