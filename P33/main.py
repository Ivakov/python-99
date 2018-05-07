def is_coprime(x,y):
    if x >= y:
        r = x % y
        if x % y == 0:
            if y == 1:
                return True 
            else:
                return False
        else:
            return is_coprime(r,y)

    if y >= x:
        r = y % x
        if y % x == 0:
            if x == 1:
                return True
            else:
                return False
        else:
            return is_coprime(x,r)
