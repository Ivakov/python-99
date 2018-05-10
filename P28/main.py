def lsort(x):
    x.sort(key=len)
    return x


def lfsort(x):
    a = []
    for i in range(len(x)): 
        if a == []:
            a.append([x[i]])
           
        else:
            is_added = False
            for j in a:
                if len(j[-1]) == len(x[i]):
                    j.append(x[i])
                    is_added = True

            if is_added == False:
                a.append([x[i]])

    a.sort(key=len)
 
    flat_a = []
    for k in a:
        flat_a = flat_a + k
    
    return flat_a 
