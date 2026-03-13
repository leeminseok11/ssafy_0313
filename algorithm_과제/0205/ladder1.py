import sys
sys.stdin = open('02_05.txt')
# 1. 값이 2인 좌표를 구하기(마지막 줄 체크 2 찾기)
# 2.
# dx =[0 0 -1] /dy =[-1 1 0] 왼 오 위 순을 탐색
# ladder (arr, x, y)
#      while :
#         if x 가0일 때 리턴
#             for i(3)
#                 nx = x +dx[i] / 다음 좌표
#                 ny = y +dy[i]
#             if 0<=nx <N and K = NY<N and arr[nx][ny] ==1 :
#                 x = nx
#                 y = ny
#                 arr[x][y] =9
def find_start(arr):
    for i in range(N):
        if arr[N-1][i] == 2:
            x = N-1
            y = i
            return x, y
def ladder(arr, x, y):
    while True:#무한대로 돌리기
     #첫줄에 이동 했을 때 y 좌표 리턴
        if x == 0: return y
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            #인덱스 체크를 먼저해야함 좌표값이 1 인 경우만 이동
            if 0<=nx<N and 0<=ny<N and arr[nx][ny]==1:
                x = nx
                y = ny
                #방문체크
                arr[x][y] = 9 #방문한곳을 9로 변환해서 체크

T = 10
N = 100
dx = [0, 0, -1]
dy = [-1, 1, 0]
for tc in range(1, T + 1):
    no = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #마지막 행에서 값이 2 인 좌표 구하기
    x, y = find_start(arr)
    #사다리를 위쪽으로 이동하기
    print(f'#{tc} {ladder(arr, x, y)}')

