import sys
sys.stdin = open('배열최소합.txt')

def f(row, k, s):
    global min_v
    global cnt
    cnt += 1

    if s >= min_v:
        return
    if row == k:
        min_v = s
        return

    for col in range(k):
        if not visited[col]:
            visited[col] = 1
            f(row + 1, k, s + arr[row][col])
            visited[col] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_v = 10000
    cnt = 0
    f(0, N, 0)
    print(f'#{tc} {min_v}')