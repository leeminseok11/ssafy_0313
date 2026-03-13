import sys
sys.stdin = open('input.txt')

def dfs(v):
    global found
    if v == 99:
        found = 1
        return

    visited[v] = 1
    for w in adj_lst[v]:
        if not visited[w]:
            dfs(w)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    adj_lst = [[] for _ in range(100)]
    visited = [0] * 100
    found = 0

    for i in range(N):
        s = data[2*i]
        e = data[2*i+1]
        adj_lst[s].append(e)

    dfs(0)
    print(f'#{tc} {found}')