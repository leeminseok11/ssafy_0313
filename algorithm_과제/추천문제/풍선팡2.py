import sys; sys.stdin = open('풍선팡2.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    for i in range(N):
        for j in range(M):
            sum = 0
            for di, dj in [[0, 1],[1, 0],[0, -1],[-1, 0]]:

                ni = di + i
                nj = dj + j
                if 0 <= ni < N and 0 <= nj < M :
                    sum += arr[ni][nj]
            total = arr[i][j] + sum

            if max_v < total :
                max_v = total
    print(f'#{tc} {max_v}')