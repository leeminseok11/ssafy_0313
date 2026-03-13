import sys;sys.stdin = open('풍선팡_input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for r in range(N):
        for c in range(M):
            sum_v = arr[r][c]
            for i in range(4): # 방향
                for j in range(1, arr[r][c] + 1): # 크기(배수)
                    nr = r + dr[i] * j
                    nc = c + dc[i] * j
                    if 0 <= nr < N and 0 <= nc < M :# 인덱스 체크
                        sum_v += arr[nr][nc]
            if ans < sum_v:
                ans = sum_v
    print(f'#{tc} {ans}')