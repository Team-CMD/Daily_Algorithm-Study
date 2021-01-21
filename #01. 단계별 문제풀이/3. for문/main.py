# print("|\_/|")
# print("|q p|   /}")
# print('( 0 )"""\\')
# print('|"^"`    |')
# print("||_/=\\\__|")

# A = input("A = ")
#
# B = input("B = ")
#
# result = int(A) + int(B)
# print("A + B = %d" %result)

# while True:
#     A, B = input().split()
#
#     if int(A) >= 0 & int(B) >= 0:
#         result = int(A) + int(B)
#         print("%d" % result)
#     break

# a = list(input().split())
#
# print(a)

# print("%d\n%d\n" %(7+3, 7-3))

# A, B, C = map(int, input().split())
# print((A+B)%C)
# print((A%C+B%C)%C)
# print((A*B)%C)
# print((A%C)*(B%C)%C)


# Num1 = input()
# Num2 = input()
#
# num1 = list(map(int, Num1))
# num2 = list(map(int, Num2))
#
# print(int(Num1) * num2[2])
# print(int(Num1) * num2[1])
# print(int(Num1) * num2[0])
#
# NUM1 = int(Num1) * num2[2]
# NUM2 = int(Num1) * num2[1]
# NUM3 = int(Num1) * num2[0]
#
# result = NUM1 + (NUM2*10) + (NUM3 * 100)
# print(result)

#2021.01.19

# A, B = map(int, input().split())
#
# if A < B:
#     print("<")
#
# elif A > B:
#     print(">")
#
# elif A == B:
#     print("==")

# A = input()
# A = int(A)
#
# if (A >= 90) & (A <= 100): #True False
#     print("A")
# elif (A >= 80) & (A <= 89):
#     print("B")
# elif (A >= 70) & (A <= 79):
#     print("C")
# elif (A >= 60) & (A <= 69):
#     print("D")
# else:
#     print("F")

# A = input()
# A = int(A)
#
# if A % 400 == 0:
#     print("1")
# elif (A % 4 == 0) & (A % 100 != 0):
#     print("1")
# else:
#     print("0")

# A = input()
# B = input()
#
# A = int(A)
# B = int(B)
#
# if (A > 0) & (B > 0):
#     print("1")
# elif (A < 0) & (B > 0):
#     print("2")
# elif (A < 0) & (B < 0):
#     print("3")
# elif (A > 0) & (B < 0):
#     print("4")

# H, M = map(int, input().split())
#
# if M - 45 < 0:
#     H = H - 1
#     M = M - 45
#     M = 60 + M
# elif M - 45 >= 0:
#     M = M - 45
#
# if H < 0:
#     H = 24 + H
#
# print(H, M)

#2021.01.21

#2739

# N = input()
# N = int(N)
#
# for i in range(1, 10):
#     print("%d * %d = %d" %(N, i, N * i))

#10950

# N = int(input())
# A = []
#
# for i in range(N):
#     a, b = map(int, input().split())
#     a = a + b
#     A.append(a)
#
# for i in range(N):
#     print(A[i])

#8393

# N = int(input())
# n = 0
#
# for i in range(1, N+1):
#     n = n + i
# print(n)

#15552

# import sys
# N = int(sys.stdin.readline())
#
# A = []
#
# for i in range(N):
#     a, b = map(int, sys.stdin.readline().split())
#     a = a + b
#     A.append(a)
#
# for i in range(N):
#     print(A[i])

#2741

# N = int(input())
#
# for i in range(1, N+1):
#     print(i)

#2742

# N = input()
# N = int(N)
# a = []

# for i in range(1, N + 1):
#     a.append(i)
#
# a.reverse()
#
# for i in range(N):
#     print(a[i])
#
# N = input()
# N = int(N)
#
# for i in range(N):
#     print(N - i)

# N = int(input())
#
# for i in range(N, 0, -1):
#     print(i)

#11021

# N = int(input())
# A = []
#
# for i in range(N):
#     a, b = map(int, input().split())
#     a = a + b
#     A.append(a)
#
# for i in range(N):
#     print("Case #%d: %d" %(i+1, A[i]))

#11022

# N = int(input())
# R = []
# A = []
# B = []
#
# for i in range(N):
#     a, b = map(int, input().split())
#     A.append(a)
#     B.append(b)
#     a = a + b
#     R.append(a)
#
# for i in range(N):
#     print("Case #%d: %d + %d = %d" %(i+1, A[i], B[i], R[i]))

#2438

# N = int(input())
#
# for i in range(1, N+1):
#     print("*"*i)
#
# #2439
#
# N = int(input())
#
# for i in range(N, 0, -1):
#     # print("/"*i)
#     for j in range(i-1):
#         print(" ", end="")
#     for j in range(N - i + 1, 0, -1):
#         print("*", end="")
#     print("")



# N = int(input())

# for i in range(N, 0, -1):
#     print(" "*(i-1), end="")
#     for j in range(N-i+1):
#         print("*", end=" ")
#     print(" ")

# for i in range(N+1):
#     # for j in range(i+1, 1, -1):
#     #     print("//")
#     for j in range(i):
#         print("*", end=" ")
#     print("")

# N = int(input())
# i = 0
# j = 0
#
# for i in range(N, 0, -1):
#     print(" "*(i-1), end="")
#     for j in range(N-i+1):
#         print("*", end="")
#     print(" ")

#10871

# N, X = map(int, input().split())
# A = list(map(int, input().split()))
#
# for i in range(0, N):
#     if (A[i] < X):
#         print(A[i], end=' ')





















