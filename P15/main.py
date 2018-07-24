def duplicate(x,y):
    ret = []
    for i in x:
        ret = ret + [i] * y
    return ret
