import sys; sys.stdin = open('초심자회문_input.txt')

T = int(input())
for tc in range(1, T+1):
    txt = input()
    N = len(txt)

    flag = 1    # 회문이라고 가정
    for i in range(N//2):  # 길이의 반만
        if txt[i] != txt[N-1-i]:  # 회문이 아닐 때를 검사
            flag = 0
            break
    print(f'#{tc} {flag}')