import re

camel = 'stringInCamelCase'
#st = input()
def toLow(ch):
    ch = ch.group(0)
    if ch.isupper():
        st = '_' + str(ch.lower())
        return st
    else:
        return ch

patt = r'[A-Z]'
print(re.sub(patt, toLow, camel))