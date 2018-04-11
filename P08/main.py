def compress(x):
    ret=[]
    for X in (x):
        if (ret==[] or ret[-1] != X):
            ret.append(X)
    return ret

