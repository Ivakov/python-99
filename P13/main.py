def encode_direct(x):
    ret = []
    for i in x:
        if ret == []:
            ret.append(i)
        elif isinstance(ret[-1],list) and ret[-1][-1] == i:
            ret[-1][0] += 1
        elif ret[-1] == i:
            ret[-1] = [2,i]
        else:
            ret.append(i)
    return ret             
