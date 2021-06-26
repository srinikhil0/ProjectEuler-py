def prime():
    n = 10001
    x =2
    lis = []
    while(len(lis))<n:
        if all(x % prime for prime in lis):
            lis.append(x)
        x += 1
    print(lis[-1])

prime()
