import sys
sys.stdin = open('sum.txt')

T = 10
for tc in range(1, T +1):
    case_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_v = 0
    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[i][j]
            if max_v < total:
                max_v = total

    for j in range(100):
        total = 0
        for i in range(100):
            total += arr[i][j]
            if max_v < total:
                max_v = total
    total = 0
    for i in range(100):
        total += arr[i][i]
        if max_v < total:
            max_v = total

    total = 0
    for i in range(100):
        total += arr[i][99-i]
        if max_v < total:
            max_v = total
    print(f'#{tc} {max_v}')