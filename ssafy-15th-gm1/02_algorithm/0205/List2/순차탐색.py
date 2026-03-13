def for_search(a, n, key):
    for i in range(n):
        if a[i] == key:
            return i
    return -1


data = [4, 9, 11, 23, 2, 19, 7]
key = 22
print(for_search(data, len(data), key))