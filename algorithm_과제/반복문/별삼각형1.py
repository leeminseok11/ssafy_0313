import sys
sys.stdin = open('반복문 연습문제.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    print(f'#{tc}')

    if M == 1:
        for i in range(1, N + 1):
            print('*' * i)
    if M == 2:
        for i in range(N, 0, -1):
            print('*' * i)
    if M == 3:
        for i in range(1, N + 1):
            print(' ' * (N - i) + '*' * (2*i - 1))