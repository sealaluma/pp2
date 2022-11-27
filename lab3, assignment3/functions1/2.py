def convertion(ftem):  
    #Fahrenheit to centigrade
    #C = (5 / 9) * (F – 32)
    ctem = int()
    ctem = (5 / 9) * (ftem - 32)
    return ctem

ftem = int(input())
print (convertion(ftem))