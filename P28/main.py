def lsort(x):
    x.sort(key=len)
    return x


def lfsort(x):
    ret=[[x[0]]]
    for i in range(1,len(x)):
        is_added = False
        for j in ret:
            if len(j[-1]) == len(x[i]):
                j.append(x[i])
                is_added = True
        if is_added == False:
            ret.append([x[i]])

    ret.sort(key=len)
    ret_A=[]
    for k in ret:
        ret_A=ret_A+k

    return ret_A
