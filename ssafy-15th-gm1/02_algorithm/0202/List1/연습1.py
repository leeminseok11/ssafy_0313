import sys
sys.stdin = open('연습1_input.txt')

T = int(input())   # 테스트케이스 갯수
for tc in range(1, T+1):
    N = int(input())   # 리스트 원소의 수
    arr = list(map(int, input().split())) # 1차원 배열 입력
    # print(arr)

    max_v = arr[0]
    min_v = arr[0]
    for i in range(N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]
    print(f'#{tc} {max_v - min_v}')
