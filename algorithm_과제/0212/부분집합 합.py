import sys;

sys.stdin = open('부분집합 합.txt')

def powerset(level):
    global ans
    if ans == 1:
        return
    if level == N:
        sum_v = 0
        k = 0
        for i in range(N):
            if path[i] == 1:
                sum_v += arr[i]
                k += 1
        if sum_v == 0 and k > 0:
            ans = 1
        return
    else:
        path[level] = 1
        powerset(level + 1)
        path[level] = 0
        powerset(level + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    path = [0] * N
    ans = 0
    powerset(0)
    print(f'#{tc} {ans}')