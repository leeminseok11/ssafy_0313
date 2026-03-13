import sys
sys.stdin = open('input_0219.txt')

def pre_order(T):   # 전위순회, 방문한 정점(부모) 먼저 처리
    global cnt
    if T:   # 0이 아니면 (존재하는 정점이면)
        cnt +=1
            # visit(T) T에서 할일 처리
        pre_order(left[T])  # 왼쪽 자식(서브트리)로 이동
        pre_order(right[T]) # 오른쪽 자식(서브트리)로 이동


T = int(input())
for tc in range(1, T+1) :
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    left = [0] * (V + 1)
    right = [0] * (V + 1)

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    cnt = 0
    pre_order(N)
    print(f'#{tc} {cnt}')

