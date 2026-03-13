def binary_search(a, n, key):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == key:
            return mid
        elif a[mid] > key: # key 값이 왼쪽 범위에 존재
            end = mid - 1
        else:   # a[mid] < key # key 값이 오른쪽 범위에 존재
            start = mid + 1
    return -1


arr = [2, 4, 7, 9, 11, 19, 23]
key = 29
print(binary_search(arr, len(arr), key))