import random
def rnd_select(x,y):
    return(random.choices(list(range(0,y+1)),k=x))
