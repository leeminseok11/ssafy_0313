import sys
sys.stdin = open('전기버스2.txt')
def dfs(now, cnt):
    global ans

    if cnt >= ans:
        return

    if now + arr[now] >= n:
        ans = min(ans, cnt)
        return

    for i in range(1, arr[now] + 1):
        dfs(now + i, cnt + 1)
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n=arr[0]
    ans = n
    dfs(1, 0)

    print(f'#{tc} {ans}')


