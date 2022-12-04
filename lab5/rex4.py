import re

st = input()
patt = r'[A-Z]{1}[a-z]+'
if re.search(patt, st):
    print('match')
else:
    print('no match')