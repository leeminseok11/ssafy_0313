import sys
sys.stdin = open('전봇대.txt')

T = int(input())
for tc in range(1, T +1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()

    cnt= 0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i][1] > arr[j][1]:
                cnt += 1

    print(f'#{tc} {cnt}')