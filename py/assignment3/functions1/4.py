def filter_prime (li): 
    li2 =[]
    for num in li1: 
        flag = True
        if num > 1: 
            for i in range(2, num): 
                if (num % i) == 0: 
                    flag = False
                    break 
            if flag:
                li2.append(num)
    return (li2) 
 
     
li1 = [] 
n = int(input()) 
for i in range (0, n): 
    m = int(input())     
    li1.append(m)
    
    
#n = int(input()) 
#li1 = [int(x) for x in input().split()] 

    
print(filter_prime(li1))