def gcd(x,y):
    if x < y:
        x,y=y,x

    r = x % y
    if r == 0:
        return y
    else:
        return gcd(r,y)
