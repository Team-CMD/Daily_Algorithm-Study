import copy

def func(arr1,arr2,ans,n):
    if sum(arr2) == 0:
        global Max
        global Min
        if ans > Max:
            Max = ans
        if ans < Min:
            Min = ans
        return

    if arr2[0]>0:
        tmp = copy.deepcopy(arr2)
        tmp[0]-=1
        func(arr1, tmp, ans + arr1[n], n + 1)
    if arr2[1]>0:
        tmp = copy.deepcopy(arr2)
        tmp[1]-=1
        func(arr1, tmp, ans - arr1[n], n + 1)
    if arr2[2]>0:
        tmp = copy.deepcopy(arr2)
        tmp[2]-=1
        func(arr1, tmp, ans * arr1[n], n + 1)
    if arr2[3]>0:
        tmp = copy.deepcopy(arr2)
        tmp[3] -= 1
        if ans<0:
            func(arr1, tmp, abs(ans) // arr1[n] * (-1), n + 1)
        else:
            func(arr1, tmp, abs(ans) // arr1[n], n + 1)
    return



N = int(input())
arr1 = list(map(int, input().split()))

arr2 = list(map(int, input().split()))

Max = -1000000000
Min = 1000000000

func(arr1,arr2,arr1[0],1)
print(Max)
print(Min)