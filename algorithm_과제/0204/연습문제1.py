import sys
sys.stdin = open('연습문제1_in.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    s = 0

    for i in range(N):
        for j in range(N):
            if i == j or (N-1-i) == j:
                s += arr[i][j]
    print(f'#{tc} {s}')
