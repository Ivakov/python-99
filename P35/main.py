import sys
sys.path.append('../')

from P31.main import is_prime

def prime_factors(x):
    ret = []
    for i in range(x+1):
        if is_prime(i):
            answers = divmod(x,i)
            if answers[1] == 0:
                print(i,answers[0])
