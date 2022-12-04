import re

st = input()
patt = r'[a-z]+_{1}[a-z]+'
if re.search(patt, st):
    print('match')
else:
    print('no match')