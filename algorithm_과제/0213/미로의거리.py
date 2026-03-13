import sys; sys.stdin = open('0213_input.txt')


def start_pos(arr):
    for i in range(N):  # 출발점 찾기
        for j in range(N):
            if arr[i][j] == 2:
                return i, j


def bfs(r, c):
    # 인큐 + 방문체크
    Q = [(r, c)]  # Q 만들어서 enQ
    visited[r][c] = 1

    while Q:
        # deQ + 할일
        r, c = Q.pop(0)
        if arr[r][c] == 3:  # 출구 만나면
            return visited[r][c] - 2  # 출발지는 칸수에서 제외
        # 인접정점(w) 미방문 이면 enQ + 방문체트
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 \
                    and arr[nr][nc] != 1:
                Q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    return 0  # 출구에 가지 못하고 모든 칸 방문


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    r, c = start_pos(arr)
    print(f'#{tc} {bfs(r, c)}')