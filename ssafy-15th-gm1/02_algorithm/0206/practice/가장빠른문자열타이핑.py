# aaaa aa 반례를 주의해야 함
# ssaa sa
# import sys
# sys.stdin = open("가장빠른문자열타이핑_input.txt")

def my_find(txt, pat, N, M):
    cnt = 0
    i = 0                       # 초기식
    # for i in range(N-M+1):
    while i < N - M +1:         # 조건식
        flag = 1
        for j in range(M):
            if txt[i+j] != pat[j]:
                flag = 0
                break
        if flag:
            cnt += 1
            i = i + M - 1       # 찾은 패턴 이후로 인덱스를 변경(뒤쪽에 증감식이 있어서 1를 뺌)
        i += 1                  # 증감식
    return cnt

T = int(input())
for tc in range(1, T+1):
    txt, pat = map(str, input().split())
    N, M = len(txt), len(pat)
    cnt = my_find(txt, pat, N, M)
    ans = N - M * cnt + cnt
    print(f'#{tc} {ans}')