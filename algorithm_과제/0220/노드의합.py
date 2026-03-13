def post_order(T):
    if T > N:
        return
    post_order(T * 2)
    post_order(T * 2 + 1)
    if T * 2 <= N:
        tree[T] += tree[T * 2]
    if T * 2 + 1 <= N:
        tree[T] += tree[T * 2 + 1]



import sys
sys.stdin = open('노드의합.txt')

T = int(input())

for tc in range(1, T + 1):

    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value

    post_order(1)
    print(f"#{tc} {tree[L]}")