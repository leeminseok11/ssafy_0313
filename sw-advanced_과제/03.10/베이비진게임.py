import sys
sys.stdin = open('베이비진게임.txt')

def check(arr):
    for i in range(10):
        if arr[i] >= 3:
            return True
    for i in range(8):
        if arr[i] >= 1 and arr[i+1] >= 1 and arr[i+2] >= 1:
            return True
    return False
T = int(input())
for tc in range(1, T+1):
    n = list(map(int, input().split()))
    p1 = [0]*10
    p2 = [0]*10
    winner = 0

    for i in range(12):
        if i % 2 == 0:
            p1[n[i]] += 1
            if i >= 4 and check(p1):
                winner = 1
                break
        else:
            p2[n[i]] += 1
            if i >= 5 and check(p2):
                winner = 2
                break
    print(f'#{tc} {winner}')




