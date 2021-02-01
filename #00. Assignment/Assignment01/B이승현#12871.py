#=========================================
#==============풀이시간 1시간==============
#=========================================

if __name__=="__main__":
    s = list(input())
    t = list(input())
    n = 0
    tmp = 1

    if len(s) > len(t):
        s=s*2
        for i in range(0,len(s)):
            if s[i] != t[n]:
                tmp = 0
            n +=1
            if n == (len(t)):
                n = 0

    elif len(s) < len(t):
        t=t*2
        for i in range(0,len(t)):
            if t[i] != s[n]:
                tmp = 0
            n+=1
            if n == (len(s)):
                n = 0

    else :
        for i in range(0,len(s)):
            if t[i] != s[i]:
                tmp = 0

    print(tmp)
