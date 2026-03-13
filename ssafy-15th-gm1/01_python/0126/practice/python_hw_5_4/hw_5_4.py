# 아래 함수를 수정하시오.
def find_min_max(arr):
    return min(arr), max(arr)


def find_min_max_2(arr):
    # 최대값, 최소값를 리스트의 첫번째 인자로 초기화
    # min_v = arr[0]
    # for num in arr:
    #     if min_v > num:
    #         min_v = num

    # max_v = arr[0]
    # for num in arr:
    #     if max_v < num:
    #         max_v = num
    
    # return min_v, max_v

    min_v = arr[0]
    max_v = arr[0]
    for num in arr:
        if min_v > num:
            min_v = num
        if max_v < num:
            max_v = num

    return min_v, max_v


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)

result = find_min_max_2([3, 1, 7, 2, 5])
print(result)  # (1, 7)
