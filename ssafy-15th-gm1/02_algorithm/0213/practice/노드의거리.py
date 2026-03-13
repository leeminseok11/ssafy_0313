import sys; sys.stdin = open('노드의거리_input.txt')

def bfs(v):
    Q = [v]         # enQ
    visisted[v] = 1
    while Q:
        v = Q.pop(0) # deQ
        # 할일 : G에 도착했으면 visited[v] 리턴
        if v == G:
            return visisted[v] - 1
        # v에 인접정점(w)가 미방문 enQ
        for w in adj_lst[v]:
            if visisted[w] == 0:
                Q.append(w)
                visisted[w] = visisted[v] + 1
    return 0  # 경로가 없으면

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_lst = [[] for _ in range(V+1)]  # 인접리스트
    visisted = [0] * (V+1)
    for _ in range(E):
        s, e = map(int, input().split())
        adj_lst[s].append(e)
        adj_lst[e].append(s)
    S, G = map(int, input().split())
    print(f'#{tc} {bfs(S)}')