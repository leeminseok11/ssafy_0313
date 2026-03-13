import sys
sys.stdin = open('퀵정렬.txt')


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    a = arr[1:]
    left = [x for x in a if x <= pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

T = int(input())
for tc in range(1, 1 + T):
    n = int(input())
    arr = list(map(int, input().split()))
    new_arr = quick_sort(arr)
    answer = new_arr[n//2]
    print(f'#{tc} {answer}')

