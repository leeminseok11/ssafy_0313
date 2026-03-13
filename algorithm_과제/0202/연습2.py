import sys
sys.stdin = open('연습2.txt')

T = int(input()) #테스트케이스 갯수
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0

    for i in range(N-1):
        cnt = 0
        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                cnt += 1
        if ans < cnt:
            ans = cnt

    print(f'#{tc} {ans}')