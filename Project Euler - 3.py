import math
def primefactor(n):
    p = []
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n%i == 0:
            p.append(int(i))
            n = n/i
    if n > 2:
        prime_factors.append(int(n))
    
    return max(p)
    
print(primefactor(600851475143))
