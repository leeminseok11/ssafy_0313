import sys;sys.stdin = open('2차원2_input.txt')
# 숫자가 붙어 있으면 split()를 빼라
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    print(arr)
