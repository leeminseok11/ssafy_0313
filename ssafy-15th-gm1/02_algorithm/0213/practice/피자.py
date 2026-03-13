import sys;sys.stdin = open('피자_input.txt')
def solve(arr) :
    # 화덕에 N개의 피자를 넣기
    Q = []
    for i in range(N):
        Q.append(i) # arr[i]
    idx = N  # 마지막에 넣은 피자번호
    while len(Q) != 1:
        # 피자를 꺼내서 치즈 확인
        pizza = Q.pop(0)
        arr[pizza] = arr[pizza] // 2
        # 치즈가 남아 있으면 다시 넣기
        if arr[pizza] != 0:
            Q.append(pizza)
        # 치즈가 다 녹았으면 다음 피자 넣기
        elif idx < M:
            Q.append(idx)
            idx += 1
    return Q.pop()


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 화덕크기, 피자수
    arr = list(map(int, input().split()))
    print(f'#{tc} {solve(arr) + 1}')