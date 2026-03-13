import sys
sys.stdin = open('색칠하기.txt')

T = int(input())
for tc in range(1, T +1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_0 = [[0] * 10 for _ in range(10)]

    for k in range(N):
        r1, c1, r2, c2, color = arr[k]

        for i in range(r1, r2+1):
            for j in range(c1, c2 + 1):
                arr_0[i][j] += color

    count = 0
    for i in range(10):
        for j in range(10):
            if arr_0[i][j] == 3:
                count += 1
    print(f'#{tc} {count}')




