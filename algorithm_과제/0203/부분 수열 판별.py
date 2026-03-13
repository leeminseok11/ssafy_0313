import sys
sys.stdin = open('부분 수열 판별.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B_point = 0

    for i in A:
        if B_point < M and i == B[B_point]:
            B_point += 1

    if B_point == M:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')


