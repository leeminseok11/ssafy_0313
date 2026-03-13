import sys
sys.stdin = open('02_05.txt')

def binary_search(P, key):
    l = 1
    r = P
    count = 0

    while True:
        count += 1
        c = (l + r) // 2

        if c == key:
            return count
        elif c > key:
            r = c
        else:
            l = c

T = int(input())

for tc in range(1, T +1):
    P, Pa, Pb = map(int, input().split())

    a = binary_search(P, Pa)
    b = binary_search(P, Pb)

    if a < b:
        print(f'#{tc} A')
    elif a > b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')

