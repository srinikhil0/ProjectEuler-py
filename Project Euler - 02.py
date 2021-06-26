n = int(input())
lis = []
lis2 = []
n1,n2 = 0,1 
count = 0
if n == 0:
    print('no output')
elif n == 1:
    print(n1)
else:
    while count<n:
        lis.append(n1)
        #print(n1)
        n3 = n1+n2
        n1 = n2 
        n2 = n3
        count+=1

for ele in lis:
    if ele%2 == 0:
        lis2.append(ele)
print(sum(lis2))
