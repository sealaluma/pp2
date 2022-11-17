a = int(input())
s = str(input())

if s == "k":
    c = int(input())
    b = float(a/1024)
    print(f"{b:.{c}f}")
else:
    print(a*1024)