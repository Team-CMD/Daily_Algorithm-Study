# <--- Boj 11729번 --->
# Siver 2, 하노이 탑 이동순서

def hanoi(n, front, end):
    if n == 1:
        print(front, end)
        return
    
    hanoi(n-1, front, 6-front-end)
    print(front, end)
    hanoi(n-1, 6-front-end, end)

    
if __name__ == "__main__":
    N = int(input())
    front = 1
    end = 3
    print(2**N-1)
    hanoi(N, front, end)
