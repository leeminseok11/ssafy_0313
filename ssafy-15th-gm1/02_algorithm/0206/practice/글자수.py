T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    max_v = 0
    for i in range(N):   # str1의 문자가 str2문자열에 몇번 나오는지 세기
        # 카운팅
        cnt = 0
        for j in range(M):
            if str1[i] == str2[j]:
                cnt += 1
        # 최대값
        if max_v < cnt:
            max_v = cnt
    # 출력
    print(f"#{tc} {max_v}")