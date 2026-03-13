import sys; sys.stdin = open('추천문제_input.txt')

T = int(input())
for tc in range(1, T +1):
    N = int(input())
    arr = list(map(int, input()))

    count = 0
    max_v = 0

    for i in range(N):
        if arr[i] == 1:
            count += 1
            if max_v < count:
                max_v = count
        else:
            count = 0

    print(f'#{tc} {max_v}')