
def palindrome(arr):  # 회문은 하나만 존재함
    # 행방향
    result = ''
    for i in range(N):
        for j in range(N - M + 1):
            flag = 1  # 회문이라고 가정하고 아닌경우를 체크
            for k in range(M // 2):
                if arr[i][j + k] != arr[i][j + M - 1 - k]:
                    flag = 0
                    break
            # 회문이면 출력
            if flag == 1:
                for k in range(M):
                    # print("{}".format(arr[i][j + k]), end="")
                    result += arr[i][j+k]
                return result
                # print()

    # 열방향
    for i in range(N):
        for j in range(N - M + 1):
            flag = 1
            for k in range(M // 2):
                if arr[j + k][i] != arr[j + M - 1 - k][i]:
                    flag = 0
                    break
            if flag == 1:
                for k in range(M):
                    # print("{}".format(arr[j + k][i]), end="")
                    result += arr[j + k][i]
                return result
                # print()


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    print(f"#{tc} {palindrome(arr)}")




