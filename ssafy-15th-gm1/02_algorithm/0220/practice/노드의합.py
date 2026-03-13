import sys;sys.stdin = open('노드의합_input.txt')

def postorder(v):
    if v <= N:
        postorder(2 * v)
        postorder(2 * v + 1)
        tree[v//2] += tree[v]
        # if tree[v] == 0:    # 가지노드 일때
        #     if 2 * v + 1 <= N:   # 오른쪽 자식이 있으면
        #         tree[v] = tree[2*v] + tree[2*v+1]
        #     else:    # 왼쪽 자식만 있으면
        #         tree[v] = tree[2*v]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value
    postorder(1)

    print(f'#{tc} {tree[L]}')