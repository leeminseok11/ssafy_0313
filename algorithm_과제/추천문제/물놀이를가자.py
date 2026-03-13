import sys
sys.stdin = open('물놀이를가자.txt')

from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input().split())) for _ in range(N)]

    total = 0
    queue = deque()
    visited = [[-1] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            queue = deque()
            if arr[i][j] == 'W':
                queue.append((i,j))
                visited[i][j] = 0


for di, dj in [[0,1].[1,0],[0,-1],[-1,0]]:
    ni = i + di
    nj = j + dj
    if 0 <= nx < N and 0 <= ny < M:
        if
