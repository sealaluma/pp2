import re

st = input()
patt = r'^a(b{2}|b{3})$'
if re.search(patt, st):
    print('match')
else:
    print('no match')