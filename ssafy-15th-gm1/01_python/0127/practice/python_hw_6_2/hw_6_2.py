# 아래 함수를 수정하시오.
def remove_duplicates_to_set(lst):
    new_set = set()
    for item in lst:
        new_set.add(item)
    return new_set


def remove_duplicates_to_set2(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
result = remove_duplicates_to_set2([1, 2, 2, 3, 4, 4, 5])
print(result)
