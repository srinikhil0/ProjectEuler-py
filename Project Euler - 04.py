def palindrome():
    lis = []
    for i in range(100,1000):
        for j in range(100,1000):
            a = i*j
            temp = a
            rev=0
            while(a>0):
                dig=a%10
                rev=rev*10+dig
                a=a//10
            if temp == rev:
                lis.append(temp)
                
    
    return max(lis)

print(palindrome())
