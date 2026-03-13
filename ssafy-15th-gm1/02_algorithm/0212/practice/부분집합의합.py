import sys;sys.stdin = open('부분집합의합_input.txt')

def powerset(lev, cursum):
    global ans
    # 가지치기
    # if ans < cursum : return

    if lev == N:
        if cursum == 0 and sum(path) != 0:
            ans = 1
            return
    else:
        path[lev] = 1
        powerset(lev + 1, cursum + arr[lev])
        path[lev] = 0
        powerset(lev + 1, cursum )

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    path = [0] * N
    ans = 0
    powerset(0, 0)
    print(f'#{tc} {ans}')