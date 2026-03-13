def dfs(v):
    visited[v] = 1
    for w in adj_lst[v]:
        if visited[w] == 0:
            dfs(w)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_lst = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for i in range(E):
        a, b = map(int, input().split())
        adj_lst[a].append(b)
    start, end = map(int, input().split())
    dfs(start)
    print(f'#{tc} {visited[end]}')