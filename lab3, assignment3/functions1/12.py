def histogram(li1):
    for num in li1:
        hist = ''
        cnt = num
        while( cnt > 0 ):
          hist += '*'
          cnt = cnt - 1
        print(hist)
    
li1 = [] 
n = int(input()) 
for i in range (0, n): 
    m = int(input())     
    li1.append(m)
    
#n = int(input()) 
#li1 = [int(x) for x in input().split()] 
    
histogram(li1)