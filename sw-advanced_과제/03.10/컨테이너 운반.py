import sys
sys.stdin = open('컨테이너 운반.txt')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w.sort(reverse=1)
    t.sort(reverse=1)
    total = 0
    cnt = 0
    for i in range(n):
        if cnt == m:
            break
        elif w[i] <= t[cnt]:
            total += w[i]
            cnt += 1
    print(f'#{tc} {total}')