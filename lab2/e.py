a = [int(x) for x in input().split()]
if len(a) < 2:
    n = a[0]
    x = int(input())
else: 
    n = a[0]
    x = a[1]
    

l = list()
for i in range(n):
    l.append(x + 2*i) 
ans = l[0]
for i in range(1, n):
    ans = ans^int(l[i])
print(ans)