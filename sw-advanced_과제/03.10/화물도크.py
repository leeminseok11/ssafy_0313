import sys
sys.stdin = open('화물도크.txt')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: x[1])
    cnt = 0
    last_end = 0
    for i in range(n):
        if arr[i][0] >= last_end:
            cnt += 1
            last_end = arr[i][1]
    print(f'#{tc} {cnt}')




