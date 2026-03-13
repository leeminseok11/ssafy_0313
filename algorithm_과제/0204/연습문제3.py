import sys
sys.stdin = open('연습문제3.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(1<<N):
        for j in range(N):
            pass