def decode(x):
    ret = []
    for X in x:
        if isinstance(X,list):
            ret = ret + [X[-1]] * X[0]
        else:
            ret.append(X)
    return ret
