def combination(size, x, right=0, temp=[]):
    ret=[]

    for i in range(right, len(x)):
        add = temp + [x[i]]

        
        if len(add) == size:
            ret = ret +[add]
        elif len(add) < size:
            ret = ret + combination(size, x, i + 1, add)

    return ret
