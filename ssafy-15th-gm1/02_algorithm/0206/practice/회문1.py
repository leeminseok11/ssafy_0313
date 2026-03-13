import sys; sys.stdin = open('회문1_input.txt')
def count_row(arr, N, M):
    cnt = 0
    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    flag = 0
                    break
            if flag : cnt += 1
    return cnt


def count_col(arr, N, M):
    cnt = 0
    for i in range(N):
        for j in range(N - M + 1):
            flag = 1
            for k in range(M // 2):
                if arr[j + k][i] != arr[j + M - 1 - k][i]:
                    flag = 0
                    break
            if flag: cnt += 1
    return cnt


T = 10
N = 8  # 행렬의 가로 세로 길이
for tc in range(1, T+1):
    M = int(input())  # 검사할 회문의 길이
    arr = [list(map(str, input())) for _ in range(N)]
    # arr = [list(input()) for _ in range(N)]
    # print(arr)
    cnt = 0
    cnt += count_row(arr, N, M)
    cnt += count_col(arr, N, M)
    print(f'#{tc} {cnt}')

