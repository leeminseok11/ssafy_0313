import sys;sys.stdin = open('연습3_input.txt')
def preorder(node):
    if node != 0:
        print(node, end=' ')
        preorder(tree[node][0])
        preorder(tree[node][1])
    return

V = int(input())    # 정점
E = V - 1           # 간선
temp = list(map(int, input().split()))
tree = [[0] * 3 for _ in range(V+1)]  # 인접리스트
for i in range(E):
    p, c = temp[2*i], temp[2*i+1]
    if tree[p][0] == 0:  #  왼쪽자식이 없으면
        tree[p][0] = c
    else:               # 왼쪽자식이 있으면
        tree[p][1] = c
    tree[c][2] = p      # 부모저장

# root 찾기
c = V
while tree[c][2] != 0:
    c = tree[c][2]
root =c

preorder(root)