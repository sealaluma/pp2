import re

st = 'StringWithoutAnySpaces'
#st = input()
patt = r'[A-Z]{1}[a-z]+'
print(' '.join(re.findall(patt, st)))