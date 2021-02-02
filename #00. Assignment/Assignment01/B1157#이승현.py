S = input()
l = list(S.upper())
l.sort()
top = 0
tmp = ""
for i in range(65,91):
    if l.count(chr(i)) > top:
        top = l.count(chr(i))
        tmp = chr(i)
    elif l.count(chr(i)) == top:
        tmp = "?"
print(tmp)