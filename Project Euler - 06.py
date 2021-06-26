def squarediff():
    lis = []
    slum = 0
    for i in range(1,101):
        lis.append(i**2)
    a = sum(lis)
    
    for i in range(1,101):
        slum = slum+i
    sumsq = slum**2
    
    diff = sumsq - a
    
    return diff
print (squarediff())
