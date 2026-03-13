import sys; sys.stdin = open('도로건설.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split)) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            di = [-1, 0, 1, 0]
            dj = [0, 1, 0, -1]

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                while 0<=ni< N and 0<=nj<N:
                    ni += ni+di[d]
                    nj += nj+dj[d]



