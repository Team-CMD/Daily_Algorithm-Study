#이규호

import math
a, b, c = map(int, input().split())
C = (c - b) / (a - b)
print(math.ceil(C))

#박병근

import sys
import math
A, B, V = map(int, sys.stdin.readline().split())
hap = (V-B) / (A-B)
print(math.ceil(hap))

#이승현

import math
A,B,C = map(int, input().split())
print(int((C-B)/(A-B))) if (C+B)%(A-B) == 0 else print( math.ceil((C-B)/(A-B)))

#조민준

day = (V-B)/(A-B)
if day == int(day):
    print(int(day))
else:
    print(int(day)+1)
#최형순

import math
d = 0
A, B, V = map(int,input().split())

d = (V-B)/(A-B)

print(math.ceil(d))