import sys
sys.stdin = open('최소생산비용.txt')

def dfs(v, total):
    global ans

    if total >= ans:
        return

    if v == N:
        ans = min(ans, total)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(v + 1, total + arr[v][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 999999
    dfs(0, 0)
    print(f'#{tc} {ans}')

