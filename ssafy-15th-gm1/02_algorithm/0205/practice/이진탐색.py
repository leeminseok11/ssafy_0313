import sys; sys.stdin = open('이진탐색_input.txt')

def binary_search(arr, key, page):
    start = 1
    end = page
    cnt = 0
    while start <= end:
        cnt += 1
        mid = (start + end) // 2
        if key == arr[mid]:
            return cnt
        elif key < arr[mid]:
            end = mid
        else:
            start = mid


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    arr = [0] + list(range(1, P+1))
    a = binary_search(arr, A, P)
    b = binary_search(arr, B, P)
    # print(a, b)
    ans = '0'
    if a > b : ans = 'B'
    if a < b : ans = 'A'

    print(f'#{tc} {ans}')