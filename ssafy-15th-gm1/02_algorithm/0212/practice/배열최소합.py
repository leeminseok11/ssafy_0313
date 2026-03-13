import sys;sys.stdin = open('배열최소합_input.txt')

def perm(lev, cursum):
    global ans
    if ans < cursum:
        return

    if lev == N:
        if ans > cursum:
            ans = cursum
    else:
        for i in range(lev, N):
            path[lev], path[i] = path[i], path[lev]
            perm(lev + 1, cursum + arr[lev][path[lev]])
            path[lev], path[i] = path[i], path[lev]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    path = list(range(N))
    # path = [i for i in range(N)]
    ans = 987654321  # 0xffffff, int(1e20) 최대값계산
    perm(0, 0)
    print(f'#{tc} {ans}')
