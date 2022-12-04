import re

st = input()
patt = r'^a.+b$'
if re.search(patt, st):
    print('match')
else:
    print('no match')