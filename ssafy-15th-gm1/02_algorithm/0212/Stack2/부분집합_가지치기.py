'''
집합 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]에서 부분집합의 합이 10인 부분집합의 개수를 출력하시오.
'''
def powerset(level, cursum):
    global ans, cnt
    cnt += 1
    ####### 가지치기 #######
    if cursum > 10: return
    ######################
    if level == N:
        if cursum == 10:
            ans += 1
    else:
        # 왼쪽에 1 넣기
        # path[level] = 1
        powerset(level + 1, cursum + arr[level])
        # 오른쪽에 0 넣기
        # path[level] = 0
        powerset(level + 1, cursum)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
path = [0] * N
ans = 0
cnt = 0
powerset(0, 0)
print(f'정답은 : {ans}, 호출횟수 : {cnt}')