def flatten(x):
    ret=[]
    for X in (x):
        if (isinstance(X, list)):
            ret = ret + X
        else:
            ret.append(X)
    return ret
