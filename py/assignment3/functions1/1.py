def convertion(gnum):  
    #gramm to ounch 
    #ounces = 28.3495231 * grams
    onum = int()
    onum = gnum * 28.3495231
    return onum

gnum = int(input())
print (convertion(gnum))