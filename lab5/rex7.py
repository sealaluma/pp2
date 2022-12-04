import re

snake = 'string_in_snake_case'
#snake = input()
def toUp(ch):
    ch = ch.group(0)
    if ch.islower():
        return re.sub(r'_', '', ch.upper())
    else:
        return ch
    
patt = r'_[a-zA-Z]'
print(re.sub(patt, toUp, snake))