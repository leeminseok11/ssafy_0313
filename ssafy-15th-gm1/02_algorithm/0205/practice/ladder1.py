import sys;sys.stdin = open('ladder1_input.txt')
def find_start(arr):
    for i in range(N):
        if arr[N-1][i] == 2:
            x = N - 1
            y = i
            return x, y


def ladder(arr, x, y):  # x: 행, y: 열
    while True:
        # 첫줄에 이동 했을 때 y좌표를 리턴
        if x == 0: return y
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스체크를 먼저하고 좌표값이 1인 경우만 이동
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 1:
                x = nx
                y = ny
                arr[x][y] = 9   # 방문체크

T = 10
N = 100
dx = [0, 0, -1]
dy = [-1, 1, 0]   # 좌우를 먼저 해야 함
for tc in range(1, T+1):
    no = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 맨 아래 행에서 값이 2인 좌표를 구하기
    x, y = find_start(arr)
    # 사다리를 위쪽으로 이동하기
    print(f'#{tc} {ladder(arr, x, y)}')