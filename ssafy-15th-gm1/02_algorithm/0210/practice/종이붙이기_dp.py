'''
3
30
50
70
'''

# f(0) = 1, f(1) = 1, f(n) = f(n-1) + 2 * f(n-2)

memo = [1, 1]
for i in range(2, 31):
    memo.append(memo[i-1] + 2*memo[i-2])

T = int(input())
for tc in range(1, T+1):
    N = int(input()) // 10
    print(f'#{tc} {memo[N]}')
