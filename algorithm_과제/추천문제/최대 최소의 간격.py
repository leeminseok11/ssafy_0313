import sys; sys.stdin = open('최대최소의간격.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_v = arr[0]
    max_v = arr[0]
    min_idx = 0
    max_idx = 0

    for i in range(N):
        if arr[i] < min_v:
            min_v = arr[i]
            min_idx = i

        if arr[i] >= max_v:
            max_v = arr[i]
            max_idx = i

    result = abs(max_idx - min_idx)

    print(f'#{tc} {result}')