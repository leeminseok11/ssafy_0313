import sys; sys.stdin = open('Flatten_input.txt')
def max_min(a):
    max_i = min_i = 0
    for i in range(1, N):
        if a[max_i] < a[i]:
            max_i = i
        if a[min_i] > a[i]:
            min_i = i
    return max_i, min_i

T = 10
for tc in range(1, T+1):
    N = 100
    dump_cnt = int(input())
    arr = list(map(int, input().split()))

    for i in range(dump_cnt):
        # 최대값 및 최소값의 인덱스
        max_i, min_i = max_min(arr)
        arr[max_i] -= 1
        arr[min_i] += 1
    # 평탄화가 끝난 다음 다시 최대값, 최소값
    max_i, min_i = max_min(arr)
    print(f'#{tc} {arr[max_i] - arr[min_i]}')