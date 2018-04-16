def drop(x,y):
    for X in x:
        if(X%y==0):
            x.remove(X)
    return x
