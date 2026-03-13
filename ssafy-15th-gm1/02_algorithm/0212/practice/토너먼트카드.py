import sys
sys.stdin = open('토너먼트카드게임_input.txt', 'r')


def win(r1, r2):
    if card[r1] == card[r2]:
        return r1
    else:
        if card[r1] == 1 and card[r2] == 2:  # 가위 vs 바위
            return r2
        elif card[r1] == 1 and card[r2] == 3:  # 가위 vs 보
            return r1
        elif card[r1] == 2 and card[r2] == 1:  # 바위 vs 가위
            return r1
        elif card[r1] == 2 and card[r2] == 3:  # 바위 vs 보
            return r2
        elif card[r1] == 3 and card[r2] == 1:  # 보 vs 가위
            return r2
        elif card[r1] == 3 and card[r2] == 2:  # 보 vs 바위
            return r1


def game(l, r):
    if l == r:
        return l
    else:
        r1 = game(l, (l + r) // 2)
        r2 = game((l + r) // 2 + 1, r)
        return win(r1, r2)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(map(int, input().split()))          # [1,  3,  2,  1]
    print('#{} {}'.format(tc, game(0, N-1)+1))