def gcd(x,y):
    r = x % y
    s = y % x
    if x > y:
        if r == 0:
            return y
        else:
            return gcd(r,y)
    elif s == 0:
        return x
    else:
        return gcd(x,s)
