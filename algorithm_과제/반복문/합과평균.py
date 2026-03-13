import sys
sys.stdin = open('반복문 연습문제.txt')

T = int(input())
for tc in range(1, T + 1 ):
    N = int(input())
    arr = list(map(int, input().split()))

    total = 0
    avg = 0

    for i in range(N):
        total += arr[i]
        avg = total / N


    print(f'#{tc} {total} {avg:.1f}')