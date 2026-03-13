import sys; sys.stdin = open('문자열비교_input.txt')
def bruet_force(text, pattern, N, M):
    for i in range(N-M+1):
        flag = 1
        for j in range(M):
            if text[i+j] != pattern[j]:
                flag = 0
                break
        if flag : return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    pattern = input()
    text = input()
    print(f'#{tc} {bruet_force(text, pattern, len(text), len(pattern))}')