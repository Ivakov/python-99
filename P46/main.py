def AND(x,y):
    return x == True and y == True

def OR(x,y):
    return x == True or y == True

def NAND(x,y):
    return x == False or y == False 

def NOR(x,y):
    return x == False and y == False

def XOR(x,y):
    return x != y

def IMP(x,y):
    return x == y or y == True

def EQ(x,y):
    return x == y

def table(x):
    return [[True, True, True], [True, False, True], [False, True, False], [False, False, False]]

