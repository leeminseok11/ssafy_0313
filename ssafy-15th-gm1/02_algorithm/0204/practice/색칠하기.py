import sys;sys.stdin = open('색칠하기_input.txt')
def print_arr(a):
    for lst in arr:
        print(*lst)

N = 10
T = int(input())
for tc in range(1, T+1):
    n = int(input())   # 색칠횟수
    arr = [[0] * N for _ in range(N)]  # 10 X 10 리스트를 0으로 초기화

    # 입력받고 색칠하기
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color
    # print_arr(arr)  # 확인하기

    # 겹친 칸수 카운팅
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')