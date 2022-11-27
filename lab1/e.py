distance, cartridges = [int(x) for x in input().split()] 
flag = True
for x in range(2, distance):
    if(distance % x == 0):
        flag = False
    

if(cartridges%2 == 0 and flag and distance<500):
    print("Good job!")
else:
    print("Try next time!")