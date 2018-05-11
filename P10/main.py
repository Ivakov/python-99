def encode(x):
    ret = []
    for i in x:
        if (ret == [] or ret[-1][-1] != i):
            ret.append([1,i])
        else:
            ret[-1][0] = ret[-1][0] + 1

    return ret

