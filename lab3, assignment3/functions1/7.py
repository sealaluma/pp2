def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i : i + 2] == [3, 3]:
            return True
    return False

li1 = [] 
n = int(input()) 
for i in range (0, n): 
    m = int(input())     
    li1.append(m)
    
#n = int(input()) 
#li1 = [int(x) for x in input().split()] 
    
print(has_33(li1))