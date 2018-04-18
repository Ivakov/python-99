def encode_direct(x):
    ret=[]
    for X in x:
        if(ret==[]):
            ret.append(X)
        elif not(isinstance(ret[-1],list)):
            if(ret[-1]==X):
                ret[-1]=[1,X]
            else:
                ret.append(X)
        if(isinstance(ret[-1],list)):
            if(ret[-1][-1]==X):
                ret[-1][0]=ret[-1][0]+1
            else:
                ret.append(X)
    return ret




