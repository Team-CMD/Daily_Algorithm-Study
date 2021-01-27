#AAAAAAAAAAAAAAAAAAAAAAAAA
# def func(a:int):
#     ans = a
#     while (a != 0):
#         ans += (a % 10)
#         a //= 10
#     return ans
#=========================
#BBBBBBBBBBBBBBBBBBBBBBBBB
def func(a:int):
    arr = list(str(a))
    for i in range(len(arr)):
        a+=int(arr[i])
    return a

if __name__== "__main__":
    nSelfNum = []
    for i in range(1,10001):#selfNum가 아닌 모든 수찾기
        nSelfNum.append(func(i))

    # 중복제거,정렬
    set(nSelfNum)
    nSelfNum.sort()

    for i in range(1,10001):
        if i not in nSelfNum: #nSelfNum 리스트에 없을경우 출력
            print(i)
