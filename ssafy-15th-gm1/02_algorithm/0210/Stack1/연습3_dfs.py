import sys; sys.stdin = open('연습3_input.txt')

def dfs(v):  # 시작정점
    global cnt
    # 방문체크(v) + 할일
    visited[v] = 1
    cnt += 1
    print(v, end=' ')
    # v에 인접한 정점(w) -> 미방문 -. dfs(w)
    for w in adj_lst[v]:
        if visited[w] == 0:
            dfs(w)


V, E = map(int, input().split())  # 정점, 간선
adj_lst = [[] for _ in range(V+1)] # 인접리스트
visited = [0] * (V+1)               # 방문리스트
temp = list(map(int, input().split()))
# 인접리스트에 저장
for i in range(E):
    s, e =  temp[2*i], temp[2*i+1]
    adj_lst[s].append(e)  # 양방향
    adj_lst[e].append(s)

cnt = 0
dfs(1)
print()
print(cnt)