import re

st = input()
print(re.sub("[ ,.]", ":", st))