import sys
sys.stdin = open('이진탐색.txt')

def binary_search(a, key):
    l = 0
    h = n-1
    dir = 0

    while l <= h:
        m = (l+h)//2
        if a[m] == key:
            return 1
        elif a[m] > key:
            if dir == 1:
                return 0
            dir = 1
            h = m -1
        else:
            if dir ==2:
                return 0
            dir = 2
            l = m +1
    return 0



T = int(input())
for tc in range(1, T + 1):
    n , m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    cnt = 0
    for i in b:
        cnt += binary_search(a, i)
    print(f'#{tc} {cnt}')