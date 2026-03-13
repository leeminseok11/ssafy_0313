arr = 'string'
print(arr.index('g'))
# print(arr.index('k'))
print(arr.find('k'))


def my_count(arr, key):
    cnt = 0
    for num in arr:
        if num == key:
            cnt += 1
    return cnt

arr = [1, 2, 2, 3, 3, 3]
print(arr.count(3))
print(my_count(arr, 3))