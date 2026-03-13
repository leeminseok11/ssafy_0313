def Binary_tree(v):
    global num
    if v > n:
        return
    Binary_tree(v * 2)
    tree[v] = num
    num += 1
    Binary_tree(v * 2 + 1)

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    tree = [0]*(n + 1)
    num = 1
    Binary_tree(1)
    print(f'#{tc} {tree[1]} {tree[n//2]}')