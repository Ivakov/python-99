def flatten(x):
    flat = []
    for i in x :
        if isinstance(i,list):
            flat = flat + flatten(i)
        else:
            flat.append(i)
    return flat
