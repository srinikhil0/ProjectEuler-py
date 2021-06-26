def multiples(a,b):
    m=[]
    for i in range(1,1000):
        if i%a==0 or i%b==0:
            m.append(i)
    return sum(m)
    
print(multiples(3,5))
