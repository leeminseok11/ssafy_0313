import sys
sys.stdin = open('이진수2.txt')

T = int(input())

for tc in range(1, T + 1):
    n = float(input())
    bin = ""
    cnt = 0
    while n > 0:
        n = n*2
        cnt += 1
        if n >= 1:
           bin += '1'
           n= n-1
        else:
            bin += '0'
        if cnt >12:
            bin = 'overflow'

            break
    print(f'#{tc} {bin}')
