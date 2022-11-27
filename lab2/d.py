n = int(input())

if n % 2 == 0: #even
    for x in range(n):
        for y in range(n):
            if x == y: print('#', end = '')
            elif x > y: print('#', end = '')
            elif x < y: print('.', end = '')
        print()
    
elif n % 2 == 1: #odd
    for x in range(n):
        for y in range(n):
            if x + y == n-1: print('#', end = '')
            elif x + y < n-1 : print('.', end = '')
            elif x + y > n-1: print('#', end = '')
        print()