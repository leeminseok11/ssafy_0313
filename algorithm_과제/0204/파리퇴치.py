import sys
sys.stdin = open('파리퇴치.txt')

T = int(input())
for tc in range(1, T +1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            s = 0
            for x in range(M):
                for y in range(M):
                    s += arr[i + x][j + y]

            if max_v < s:
                max_v = s

    print(f'#{tc} {max_v}')
