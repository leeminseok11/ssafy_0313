import sys;sys.stdin = open('풍선팡2_input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 2차원 배열 순회
    ans = 0
    for r in range(N):
        for c in range(M):
            sum_v = arr[r][c]  # 현재 위치도 포함
            for i in range(4): # 4방향
                nr = r + dr[i]
                nc = c + dc[i]
                # 인덱스 체크
                if 0 <= nr < N and 0 <= nc < M:
                    sum_v += arr[nr][nc]
            if ans < sum_v:
                ans = sum_v
    print(f'#{tc} {ans}')