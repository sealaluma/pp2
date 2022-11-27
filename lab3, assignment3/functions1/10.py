def unique(li1):
    li2 =[]
    for num in li1: 
        if num not in li2:
            li2.append(num)
    return (li2)

li1 = [] 
n = int(input()) 
for i in range (0, n): 
    m = int(input())     
    li1.append(m)
    
#n = int(input()) 
#li1 = [int(x) for x in input().split()] 
    
print(unique(li1))