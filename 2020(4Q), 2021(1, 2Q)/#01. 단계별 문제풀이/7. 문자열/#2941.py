CRO = input()
WORD = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in WORD:
    CRO = CRO.replace(i, "1")
print(len(CRO))