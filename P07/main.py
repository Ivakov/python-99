def flatten(x):
    ret=[]
    for X in (x):
        if (isinstance(X, list)):
            ret = ret + flatten(X)
        else:
            ret.append(X)
    return ret

