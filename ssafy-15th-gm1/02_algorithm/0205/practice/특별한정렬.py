import sys; sys.stdin = open('특별한정렬_input.txt')

def selection(arr, k):
    for i in range(k):
        m_idx = i
        if i % 2 == 0:
            for j in range(i+1, N):
                if arr[m_idx] < arr[j]:
                    m_idx = j
        else:
            for j in range(i + 1, N):
                if arr[m_idx] > arr[j]:
                    m_idx = j
        arr[i], arr[m_idx] = arr[m_idx], arr[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    selection(arr, 10)
    # print(f'#{tc}', end=' ')
    # for i in range(10):
    #     print(arr[i], end=' ')
    # print()

    print(f'#{tc}', *arr[:10])