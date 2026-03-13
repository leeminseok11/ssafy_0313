import sys; sys.stdin = open('반복문 연습문제.txt')

T = int(input())
for tc in range(1, T + 1):
    s, e = map(int, input().split())
    print(f'#{tc}')
    for i in range(s, e+1):
        for j in range(1, 10):
            print(f'{i} * {j} = {i * j:2d}', end= "   ")
            if j == 3 or j == 6:
                print()
        print()
        print()