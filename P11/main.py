def encode_modified(x):
    ret = []
    for i in x:
        if ret == [] or ret[-1][-1] != i:
            ret = ret + [[i]]
        else:
            ret[-1].append(i)
        retA = []
        for j in ret:
            if len(j) == 1:
                retA = retA + j
            else:
                retA = retA + [[len(j),j[0]]]
    return retA
