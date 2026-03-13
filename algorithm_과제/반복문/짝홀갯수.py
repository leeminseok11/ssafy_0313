import sys
sys.stdin = open('반복문 연습문제.txt')

T = int(input())
for tc in range(1, T +1):
    N = int(input())
    arr = list(map(int, input().split()))

    count_1 = 0
    count_2 = 0

    for i in range(N):
        if arr[i] % 2 == 0:
            count_1 += 1
        else:
            count_2 += 1

    print(f'#{tc} {count_1} {count_2}')