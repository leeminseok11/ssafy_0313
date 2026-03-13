import sys
sys.stdin= open('최소합.txt')

def dfs(i, j, total):
    global min_sum
    if total >= min_sum:
        return

    if i == n-1 and j == n-1:
        min_sum = min(min_sum , total)
        return

    for di, dj in [[0,1],[1,0]]:
        ni = i + di
        nj = j + dj
        if 0<=ni<n and 0<=nj<n:
            dfs(ni,nj,total + arr[ni][nj])

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 999999
    dfs(0,0,arr[0][0])
    print(f'#{tc} {min_sum}')




