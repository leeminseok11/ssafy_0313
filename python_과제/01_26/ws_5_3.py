# 아래 함수를 수정하시오.
def sort_tuple(s):
    new_tuple = ()
    i = list(s)
    i.sort()
    new_tuple = tuple(i)
    
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
