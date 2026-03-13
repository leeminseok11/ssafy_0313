import sys; sys.stdin = open('풍선팡.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    for i in range(N):
        for j in range(M):
            s = 0

            k = arr[i][j]


            for di, dj in [[0, 1],[1, 0],[0, -1],[-1, 0]]:
                for w in range(1, k + 1):
                    ni = di*w + i
                    nj = dj*w + j

                    if 0 <= ni < N and 0 <= nj < M :
                        s += arr[ni][nj]
                total = arr[i][j] + s

            if max_v < total :
                max_v = total
    print(f'#{tc} {max_v}')