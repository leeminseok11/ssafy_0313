import sys
sys.stdin = open('단순2진암호코드.txt')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(n)]

    for i in range(n-1, -1 , -1):
        for j in range(m-1, -1, -1):
            if arr[i][j] == 1:
                code = arr[i][j-55:j+1]
                break
            else:
                continue
            break
    mapping = {
        (0, 0, 0, 1, 1, 0, 1): 0, (0, 0, 1, 1, 0, 0, 1): 1, (0, 0, 1, 0, 0, 1, 1): 2,
        (0, 1, 1, 1, 1, 0, 1): 3, (0, 1, 0, 0, 0, 1, 1): 4, (0, 1, 1, 0, 0, 0, 1): 5,
        (0, 1, 0, 1, 1, 1, 1): 6, (0, 1, 1, 1, 0, 1, 1): 7, (0, 1, 1, 0, 1, 1, 1): 8,
        (0, 0, 0, 1, 0, 1, 1): 9
    }

    a = []
    for i in range(0, 56, 7):
        b = tuple(code[i:i+7])
        a.append(mapping[b])

    if ((a[0] + a[2] + a[4] + a[6])*3 + (a[1] + a[3] + a[5] + a[7])) % 10 == 0:
        print(f"#{tc} {sum(a)}")
    else:
        print(f"#{tc} {0}")

