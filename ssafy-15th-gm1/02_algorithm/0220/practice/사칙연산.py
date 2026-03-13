import sys;sys.stdin = open('사칙연산_input.txt')
def calc(op, left, right):
    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    elif op == '*':
        return left * right
    elif op == '/':
        return left / right

def postorder(v):
    if tree[v][0] == 0 and tree[v][1] == 0:  # 리프노드
        return tree[v][2]
    left = postorder(tree[v][0])
    right = postorder(tree[v][1])
    tree[v][2] = calc(tree[v][2], left, right)
    return tree[v][2]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [[0] * 3 for _ in range(N+1)] # 왼쪽,오른쪽, 연산자 또는 값

    for _ in range(N):
        tmp = list(input().split())
        idx = int(tmp[0])  # 정점번호
        if tmp[1] == '+' or tmp[1] == '-' or tmp[1] == '*' or tmp[1] == '/' :
            # tmp[1] in '+-*/'
            tree[idx][2] = tmp[1]   # 연산자
            tree[idx][0] = int(tmp[2]) # 왼쪽자식
            tree[idx][1] = int(tmp[3]) # 오른쪽자식
        else:
            tree[idx][2] = int(tmp[1])  #

    ans = postorder(1)
    print(f'#{tc} {int(ans)}')