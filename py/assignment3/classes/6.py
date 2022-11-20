def PrimeChk(n):
    if (n == 1 or n == 0) :
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True

a = int(input())
n = 0 + a
li1 = []        
for di in range (n+1):
    li1.append(i)
     
result = list(filter(lambda a : PrimeChk(a), li1))
print(result)