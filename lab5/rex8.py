import re

st = 'StringToTestThisCase'
#st = input()
patt = r'([A-Z]{1}[a-z]+)' 
print(re.split(patt, st))