# 아래 함수를 수정하시오.
def remove_duplicates_to_set(arr):
    unique_list = []          

    for item in arr:          # item : int
        if item not in unique_list:
            unique_list.append(item)

    return set(unique_list)   # list → set 변환


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)