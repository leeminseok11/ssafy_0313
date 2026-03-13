import sys
sys.stdin = open('Flatten.txt')

for tc in range(1, 11):
    N = int(input())
    a = list(map(int, input().split()))

    for _ in range(N):
        max_val = a[0]
        min_val = a[0]
        max_idx = 0
        min_idx = 0

        for i in range(100):
            if a[i] > max_val:
                max_val = a[i]
                max_idx = i
            if a[i] < min_val:
                min_val = a[i]
                min_idx = i

        a[max_idx] -= 1
        a[min_idx] += 1

    max_val = a[0]
    min_val = a[0]

    for i in range(100):
        if a[i] > max_val:
            max_val = a[i]
        if a[i] < min_val:
            min_val = a[i]

    print(f"#{tc} {max_val - min_val}")