import sys
sys.stdin = open('view.txt')

T = 10  # 테스트케이스 개수
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0

    # 양 끝 2칸 제외
    for i in range(2, N - 2):

        max_height = arr[i - 2]

        for j in (i - 1, i + 1, i + 2):
            if arr[j] > max_height:
                max_height = arr[j]

        if arr[i] > max_height:
            result += arr[i] - max_height

    print(f'#{tc} {result}')
