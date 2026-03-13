'''
집합 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]에서 부분집합의 합이 10인 부분집합의 개수를 출력하시오.
'''
def powerset(level):
    global ans, cnt
    cnt += 1
    if level == N:
        # 각 부분집합의 합을 계산
        sum_v = 0
        for i in range(N):
            if path[i] == 1:
                sum_v += arr[i]
        # 합이 10인경우 출력
        if sum_v == 10:
            ans += 1
    else:
        # 왼쪽에 1 넣기
        path[level] = 1
        powerset(level + 1)
        # 오른쪽에 0 넣기
        path[level] = 0
        powerset(level + 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
path = [0] * N
ans = 0
cnt = 0
powerset(0)
print(f'정답은 : {ans}, 호출횟수 : {cnt}')