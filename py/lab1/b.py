sum = int(0)
for x in str(input()):
    sum = sum + ord(x)
if sum > 300:
    print("It is tasty!")
else:
    print("Oh, no!")