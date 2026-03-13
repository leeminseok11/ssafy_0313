def selection_sort(a, n):
    for i in range(n-1):    # 0 ~ n-2
        # 최소값의 인덱스
        min_idx = i
        for j in range(i+1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] =  a[min_idx], a[i]    # 자리 교환


arr = [64, 25, 10, 22, 11]
selection_sort(arr, len(arr))   # 파괴적 함수
print(arr)