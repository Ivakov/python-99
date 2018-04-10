def lsort(x):
	x.sort(key=len)
	return x


def lfsort(x):
    x.sort(key=len)
    ret=[]
    for X in x:
        if(ret==[]):
            ret.append([X])
        elif(len(ret[-1][-1])==len(X)):
            ret[-1].append(X)
        else:
            ret.append([X])

    ret.sort(key=len)
    retA=[]
    for Y in ret:
        retA=retA+Y

    return retA

