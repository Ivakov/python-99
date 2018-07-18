def pack(x):
    ret = []
    for i in x:
        if ret == [] or ret[-1][-1] != i:
            ret.append([i])
        else:
            ret[-1].append(i)
    return ret
