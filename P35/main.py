def prime_factors(x):
    ret = []
    i = 2
    while i <= x:
        j,k = divmod(x,i)
        if k == 0:
            ret.append(i)
            x = j
        else:
            i = i + 1
    return ret
