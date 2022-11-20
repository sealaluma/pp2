import math

def volume(n):
    vol = (4 / 3) * pow(n, 3) * math.pi
    return vol

r = int(input())
print(volume(r))