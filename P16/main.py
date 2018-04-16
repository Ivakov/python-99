def drop(x,y):
    ret=[]
    for X in x:
        if(x[X-1] % y != 0):
            ret=ret+[X]
    return ret
