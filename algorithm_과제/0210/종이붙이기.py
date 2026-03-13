import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    dp = [0] * (N + 1)
    dp[0] = 1
    dp[10] = 1

    for i in range(20, N + 1, 10):
        dp[i] = dp[i-10] + 2 * dp[i-20]

    print(f'#{tc} {dp[N]}')