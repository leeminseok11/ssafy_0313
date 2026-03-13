import sys; sys.stdin = open('미로_input.txt', 'r')

def maze(r, c):
    global flag
    if arr[r][c] == 3:  # 도착하면
        flag = 1
        return

    visited[r][c] = 1  # 방문표시
    # 네방향 탐색
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] != 1:
            maze(nr, nc)

def findStart(arr):
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                return r, c

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    flag = 0
    sr, sc = findStart(arr)
    maze(sr, sc)
    print(f"#{tc} {flag}")
