def powering (N):
    for i in range (N + 1):
        yield i**2
        
N = int(input())
for i in powering(N):
    print (i)
    