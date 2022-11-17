s = str(input())
t = str(input())
cnt = int(-1)

if s.rfind(t) != -1:
    indexL = s.rfind(t)
    for x in s:
        cnt += 1
        if x == t and cnt != indexL:
            indexF = cnt
            break
        else:
            indexF = -1
    if indexF != -1 and indexL != indexF:
        print(str(indexF) + " " + str(indexL))
    else:
        print(indexL)