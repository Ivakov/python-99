def is_prime(x): 
    if x < 2:
        return False
       
    for y in range(2,x):
        if x % y == 0:
            return False
        
    return True 
