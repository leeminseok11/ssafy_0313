# 아래 함수를 수정하시오.
def find_min_max(numbers):
    return (min(numbers), max(numbers))

def find_min_max2(arr):
    min_v = arr[0]
    max_v = arr[0]
    for i in arr:
        if min_v > i :
            min_v = i
    
        if max_v < i :
            max_v = i
    return min_v, max_v                


#result = find_min_max([3, 1, 7, 2, 5])
result2 = find_min_max2([3, 1, 7, 2, 5])

#print(result)  # (1, 7)
print(result2)  # (1, 7)