import sys
sys.stdin = open('숫자 카드.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = input().strip()

    cnt = [0] * 10

    for c in A:
        cnt[int(c)] += 1

    max_cnt = 0
    num = 0

    for i in range(10):
        if cnt[i] > max_cnt or (cnt[i] == max_cnt and i > num):
            max_cnt = cnt[i]
            num = i

    print(f"#{tc} {num} {max_cnt}")




