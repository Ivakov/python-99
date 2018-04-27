def lsort(x):
    x.sort(key=len)
    return x


def lfsort(x):
    ret=[[x[0]]]
    for i in range(1,len(x)):
        is_added = False
        for X in ret:
            if len(X[-1]) == len(x[i]):
                X.append(x[i])
                is_added = True
        if is_added == False:
            ret.append([x[i]])

    ret.sort(key=len)
    retA=[]
    for Y in ret:
        retA=retA+Y

    return retA
