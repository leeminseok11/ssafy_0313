# 함수 정의
def get_sum(num1, num2):  # 매개변수
    pass
    return num1 + num2 

# 함수 호출 및 반환 값 할당
a = 33
b = 4
print(get_sum(a, b)) # 인자
print(get_sum(5, 6))
result = get_sum(444,555)
print(get_sum(15, 6666))

# [번외] print() 함수는 반환값이 없다.
result = print('abc') # None
print(result)