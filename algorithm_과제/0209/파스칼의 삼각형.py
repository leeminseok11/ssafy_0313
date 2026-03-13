import sys; sys.stdin = open('stack_1.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f"#{tc}")

    a = []

    for i in range(N):
        b = [1] * (i + 1)

        for j in range(1, i):
            b[j] = a[i-1][j-1] + a[i-1][j]

        a.append(b)

    for b in a:
        print(" ".join(map(str, b)))