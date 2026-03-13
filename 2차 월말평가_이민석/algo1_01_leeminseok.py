import sys
sys.stdin = open('algo1_sample_in.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2: #술래 발견시
                for d in range(4): #4방향 탐색
                    ni = di[d] + i
                    nj = dj[d] + j
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1: # 격자 범위 내 or 1 만나면
                        if arr[ni][nj] == 0: #감시 영역을 -1로 변경
                            arr[ni][nj] = -1
                        ni += di[d]
                        nj += dj[d]

    count = 0
    #총 0의 갯수 구하기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                count += 1

    print(f'#{tc} {count}')