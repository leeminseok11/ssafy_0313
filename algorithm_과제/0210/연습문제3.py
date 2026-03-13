
def dfs(v):#시작정점
    #방문체크 +할일하기
    global cnt
    visited[v] =1
    cnt += 1
    print(v, end=' ')
    #v에 인접한 정점(w)
    for w in adj_lst[v]:
        if visited[w] == 0:
            dfs(w)

V, E = map(int, input().split()) # 정점, 간선
adj_lst = [[] for _ in range(V + 1)] #인접리스트
visited = [0] *(V+1) #방문 리스트
temp = list(map(int, input().split()))
#인접리스트에 저장
for i in range(E): #간선의 갯수만큼
    s, e = temp[2*i], temp[2*i+1] #2개씩 짜르는 것 (인덱스 값을)
    adj_lst[s].append(e)
    adj_lst[e].append(s) #양방향 저장
cnt = 0
dfs(1)
print()
print(cnt)