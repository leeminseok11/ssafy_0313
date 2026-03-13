import sys
sys.stdin = open('전자카트.txt')

def dfs(now, cnt, total):
    global ans

    if total >= ans:
        return
    if cnt == n-1:
        ans = min(ans, total + arr[now][0])
        return
    for i in range(1, n):
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1, total + arr[now][i])
            visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [0]*n
    ans = 999999
    dfs(0,0,0)

    print(f"#{tc} {ans}")
