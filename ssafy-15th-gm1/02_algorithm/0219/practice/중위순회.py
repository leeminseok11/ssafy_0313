import sys; sys.stdin = open('중위순회_input.txt')

def inorder(v):
    global ans
    if v <= N:
        inorder(2*v)
        ans += tree[v]
        inorder(2*v+1)

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [''] * (N+1)
    for i in range(N):
        temp = input().split()
        idx = int(temp[0])
        tree[idx] = temp[1]

    ans = ''
    inorder(1)
    print(f'#{tc} {ans}')