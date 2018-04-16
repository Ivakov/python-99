def split(x,y):
    ret=[]
    if(y==0):
       ret=[[],x]
    else:
        ret=[x[:y],x[y:]]   
    return ret
    
