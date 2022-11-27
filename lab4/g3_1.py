def twelve(n):
    for i in range (0, n + 1): # or in range (1, n + 1), if so, 0 is not included
        if i % 3 == 0 and i % 4 == 0:
            yield i
            
n = int(input())
for i in twelve(n):
    print (i)