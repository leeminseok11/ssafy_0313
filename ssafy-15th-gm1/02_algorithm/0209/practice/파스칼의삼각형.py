import sys; sys.stdin = open('파스칼의삼각형_input.txt')

SIZE = 11
memo = [[0] * SIZE for _ in range(SIZE)]
for i in range(SIZE):
    for j in range(i+1):
        if i == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j]
# print(memo[3][3])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(f'{memo[i][j]}', end=' ')
        print()