def powerset(level):
    if level == N:
        print(path)
    else:
        # 왼쪽에 1 넣기
        path[level] = 1
        powerset(level + 1)
        # 오른쪽에 0 넣기
        path[level] = 0
        powerset(level + 1)

arr = [1, 2, 3]
N = len(arr)
path = [0] * N
powerset(0)