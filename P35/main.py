def prime_factors(x):
    ret = []
    i = 2
    while i <= x:
        a,b = divmod(x,i)
        if b == 0:
            ret.append(i)
            x = a
        else:
            i = i + 1
    return ret
