import sys; sys.stdin = open("전기버스_input.txt")

def solve(charge, k, n, m):
    charge = [0] + charge + [n]  # 출발점과 도착점 추가

    last = 0  # 마지막 충전기
    cnt = 0  # 충전횟수
    for i in range(1, m + 2):
        if charge[i] - charge[i - 1] > k:  # 충전기 사이가 k보다 크면 충전할 수 없음
            return 0
        if charge[i] > last + k:  # 충전할 수 없는 경우 앞쪽에서 충전
            last = charge[i - 1]
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    # K : 한번 충전으로 이동할 수 있는 정류장 수
    # N : 정류장 수
    # M : 충전기 설치된 정류장 번호
    K, N, M = map(int, input().split())  # 1 ≤ K, N, M ≤ 100
    charge = list(map(int, input().split()))
    ans = solve(charge, K, N, M)
    print(f'#{tc} {ans}')