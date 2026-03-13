my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.
for key in my_set:
    # print(my_dict[key])      # 키값이 없으면 에러 
    print(my_dict.get(key))    # 키값이 없으면 None

var = (1, 2, 3, 'A')   # 튜플도 불변자료형이므로 딕셔너릴의 키로 사용가능
my_dict[var] = '변수로도 키 설정 가능'
print(my_dict)