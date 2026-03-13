import sys
sys.stdin = open('연습문제2.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0

    for i in range(N):
        for j in range(N):
            s = 0
            for di, dj in [[0, 1],[1, 0],[0, -1],[-1, 0]]:
                ni, nj = i+di, j+dj

                if 0 <= ni < N and 0 <= nj < N:
                    k = arr[ni][nj] - arr[i][j]
                    if k <= 0:
                        k = -k
                    s += k

            total += s

    print(f'#{tc} {total}')