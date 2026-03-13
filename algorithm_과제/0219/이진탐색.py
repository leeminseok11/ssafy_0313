import sys
sys.stdin = open('input_0219.txt')

def inorder(v):
    global num
    if v <= N:
        inorder(2*v)
        tree[v] = num
        num += 1
        inorder(2*v+1)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #1차원에 저장할 배열
    tree = [0]*(N + 1) #인덱스0은 안쓰므로
    num = 1
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')