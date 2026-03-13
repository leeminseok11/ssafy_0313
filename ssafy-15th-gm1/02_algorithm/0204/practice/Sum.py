import sys;sys.stdin = open('Sum_input.txt')

T = 10
for tc in range(1, T+1):
    no = int(input())  # 받아서 안 씀
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0   # 정답
    # 행우선
    for i in range(N):
        total = 0   # 각행의 합
        for j in range(N):
            total += arr[i][j]
        if max_v < total:
            max_v = total

    # 열우선
    for i in range(N):
        total = 0   # 각행의 합
        for j in range(N):
            total += arr[j][i]
        if max_v < total:
            max_v = total
    # 대각선 \
    total = 0
    for i in range(N):
        total += arr[i][i]
    if max_v < total:
        max_v = total

    # 대각선 /
    total = 0
    for i in range(N):
        total += arr[i][N-1-i]
    if max_v < total:
        max_v = total

    print(f'#{tc} {max_v}')