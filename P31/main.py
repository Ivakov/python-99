def is_prime(x,index=2):
    if x < 2:
        return False
    else:
        is_judge = True        
        for y in range(index,x):
            if (x % y == 0):
                return False
                is_judge = False
        if is_judge == True:
            return True 
