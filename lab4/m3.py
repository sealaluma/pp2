import math

n = int(input())
ls = int(input())
aph = ls / (2 * math.tan(math.pi / n ))
A = (n * ls * aph) / 2

print ("Input number of sides: ", n)
print ("Input the length of a side: ", ls)
print ("The area of the polygon is: ", float(A))

#print(float((numb_of_sides*len_of_side**2*(math.tan(math.pi/numb_of_sides)**-1))/4))