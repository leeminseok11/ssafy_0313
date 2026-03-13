import sys
sys.stdin = open('중력_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for i in range(N-1): # 마지막은 검사 생략
        cnt = 0
        # i 이후의 모든 행을 검사
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt += 1
        #cnt의 최대값 구하기
        if ans < cnt:
            ans = cnt
    print(f'#{tc} {ans}')

