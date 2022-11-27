def spy_game(nums):
    spy = 0
    for x in range(0,len(nums)-2):
        if nums[x] == 0 and nums[x+1] == 0 and nums[x+2]==7:
            return True
    return False

li1 = [] 
n = int(input()) 
for i in range (0, n): 
    m = int(input())     
    li1.append(m)
    
#n = int(input()) 
#li1 = [int(x) for x in input().split()] 
    
print(spy_game(li1))