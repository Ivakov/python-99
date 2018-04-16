def encode_modified(x):
    ret=[]
    for X in x:
        if(ret==[] or ret[-1][-1]!=X):
            ret=ret+[[X]]
        else:
            ret[-1].append(X)
        retA=[]
        for Y in ret:
            if(len(Y)==1):
                retA=retA+Y
            else:
                retA=retA+[[len(Y),Y[0]]]
    return retA
