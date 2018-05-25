import itertools


def AND(x,y):
    return x & y 

def OR(x,y):
    return x | y

def NAND(x,y):
    return not x & y

def NOR(x,y):
    return not x | y

def XOR(x,y):
    return x ^ y

def IMP(x,y):
    return (x == y) | y

def EQ(x,y):
    return x == y

def table(formula):
    truth_table = []
    for a,b in itertools.product([True,False], repeat=2):
        truth_table.append([a,b,formula(a,b)])
    return truth_table
