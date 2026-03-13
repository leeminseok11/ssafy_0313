def perm(lev):
    if lev == N:
        print(path)
    else:
        for i in range(lev, N):
            path[i], path[lev] = path[lev], path[i]
            perm(lev+ 1)
            path[i], path[lev] = path[lev], path[i]


path = [0, 1, 2]  # 순열의 결과(실제로는 인덱스로 활용됨)
N = len(path)
perm(0)