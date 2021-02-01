#===================================
#           소요시간 30분
#===================================

s = input()
t = input()

tmp = len(s)*len(t)
s_check = s*len(t)
t_check = t*len(s)

if len(s) != len(t):
    if s_check == t_check:
        print("1")
    else:
        print("0")

else:
    if s_check == t_check:
        print("1")
    else:
        print("0")