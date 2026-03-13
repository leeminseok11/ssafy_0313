import sys;sys.stdin = open('숫자카드_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))  # 숫자가 붙어있어서 split뺌
    # print(arr)

    # 카운팅
    cnts = [0] * 10
    for i in range(N):
        cnts[arr[i]] += 1
    # print(cnts)

    # 최대값의 인덱스
    max_i = 0
    for i in range(1, 10):
        if cnts[max_i] <= cnts[i]:
            max_i = i

    print(f'#{tc} {max_i} {cnts[max_i]}')

