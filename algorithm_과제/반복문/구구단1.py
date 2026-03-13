import sys; sys.stdin = open('반복문 연습문제.txt')

T = int(input())

for tc in range(1, T + 1):
    s, e = map(int, input().split())
    print(f"#{tc}")

    # 단 범위 결정
    if s <= e:
        dan_range = range(s, e + 1)
    else:
        dan_range = range(s, e - 1, -1)

    # 1 ~ 9 곱
    for i in range(1, 10):
        line = []
        for dan in dan_range:
            line.append(f"{dan} * {i} = {dan*i:2d}")
        print("   ".join(line))