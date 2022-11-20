def palCheck(s):
    return s == s[::-1]

s = input()
pal = palCheck(s)
if pal:
    print("Yes")
else:
    print("No")