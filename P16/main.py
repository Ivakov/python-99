def drop(x,y):
    ret=[]
    for i in range(len(x)):
        if((i+1) % y != 0):
            ret.append(x[i])
    return ret 
