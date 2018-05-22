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

def table(formula):
    truth_table = []
    truths_a = [True,True,False,False]
    truths_b = [True,False,True,False]
    for i in range(4):
        a = truths_a[i]
        b = truths_b[i]
        truth_table.append([a,b,formula(a,b)])
    return truth_table
