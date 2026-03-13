import sys; sys.stdin = open('반복문 연습문제.txt')
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print("#{}".format(tc))

    arr = [[0] * N for _ in range(N)]
    cnt = 0

    for j in range(N):
        if j % 2 == 0:
            for i in range(N):
                arr[i][j] = chr(ord('A') + cnt % 26)
                cnt += 1
        else:
            for i in range(N - 1, -1, -1):
                arr[i][j] = chr(ord('A') + cnt % 26)
                cnt += 1

    for i in range(N):
        print(" ".join(arr[i]))