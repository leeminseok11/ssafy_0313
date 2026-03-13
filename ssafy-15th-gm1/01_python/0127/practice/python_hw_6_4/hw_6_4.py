# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, key, value):
    new_dict = dictionary.copy()
    new_dict.update({key:value})
    return new_dict

def add_item_to_dict2(key, value):
    # 키가 없으면 추가, 있으면 수정
    my_dict[key] = value
    value = 'Japan'


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
nation = 'USA'
add_item_to_dict2('country', nation)
print(my_dict)
nation = 'Korea'
add_item_to_dict2('country', nation)
print(my_dict)


# 매개 변수 전달 방법
# - call by value : 값을 복사, 불변변수(string, tuple, int, float), 원본 수정 안됨
  
# - call by reference : 주소값을 복사, 가변변수(list, dict, ...), 원본 수정 됨
