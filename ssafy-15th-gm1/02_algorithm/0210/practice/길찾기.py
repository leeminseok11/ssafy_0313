import sys;sys.stdin = open('길찾기_input.txt')
def dfs(v):
    visited[v] = 1
    for w in adj_lst[v]:
        if visited[w] == 0:
            dfs(w)

V = 100
T = int(input())
for tc in range(1, T+1):
    E = int(input())
    temp = list(map(int, input().split()))
    adj_lst = [[] for _ in range(V)]    # 인접행렬
    visited = [0] * V
    for i in range(E):
        s, e = temp[2*i], temp[2*i+1]
        adj_lst[s].append(e)  # 단방향

    dfs(0)
    print(f'#{tc} {visited[99]}')