import sys
sys.stdin = open('구간합_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(N, M)
    # print(arr)

    min_v = 10000 * M       # 큰 값 987654321  float('inf')
    max_v = 0               # 작은 값 -987654321
    for i in range(N-M+1):
        sum_v = 0
        # 구간의 합 구하기
        for j in range(M):
            sum_v += arr[i+j]
        # 구간합의 최대값, 최소값
        if max_v < sum_v:
            max_v = sum_v
        if min_v > sum_v:
            min_v = sum_v
    print(f'#{tc} {max_v - min_v}')
