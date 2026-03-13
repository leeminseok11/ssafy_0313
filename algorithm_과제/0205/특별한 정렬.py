import sys
sys.stdin = open('02_05.txt')

T = int(input())
for tc in range(1, T +1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        min_idx = i
        for j in range(i + 1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    result = []
    left = 0
    right = N - 1

    while len(result) < 10:
        result.append(arr[right])
        result.append(arr[left])
        right -= 1
        left += 1

    print(f'#{tc}', *result)
