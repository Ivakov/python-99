def gcd(x,y):
    if x >= y:
        r = x % y
        if x % y == 0:
            return y
        else:
            return gcd(r,y)

    if y >= x:
        r = y % x
        if y % x == 0:
            return x
        else:
            return gcd(x,r)
