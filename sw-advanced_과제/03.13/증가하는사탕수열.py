import sys
sys.stdin = open('증가하는사탕수열.txt')

T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    cnt = 0

    if C <= 2:
        print(f'#{tc} -1')
        continue

    if B >= C:
        cnt += B - (C - 1)
        B = C - 1

    if A >= B:
        cnt += A - (B - 1)
        A = B - 1

    if A <= 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {cnt}')


