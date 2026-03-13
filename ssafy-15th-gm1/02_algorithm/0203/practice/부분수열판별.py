import sys; sys.stdin = open('부분수열판별_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 1. for 문
    # ans = 'NO'   # 반복문에서 정답 만나면 'YES'
    # j = 0 # B 리스트를 가르키는 포인터
    # for i in range(N): # A리스트를 가르키는 포인터(매번 증가)
    #     # j는 A[i]와 B[j]가 일치하면 증가
    #     if A[i] == B[j]:
    #         j += 1
    #     # j가 B의 모든 문자열에 일치(j == M)
    #     if j == M:
    #         ans = 'YES'
    #         break
    # print(f'#{tc} {ans}')

    # 2. while 문
    ans = 'NO'
    i, j = 0, 0    # 초기식
    while i < N and j < M: # 조건식
        if A[i] == B[j]:
            j += 1
        if j == M:
            ans = 'YES'
            break
        i += 1      # 증감식
    print(f'#{tc} {ans}')