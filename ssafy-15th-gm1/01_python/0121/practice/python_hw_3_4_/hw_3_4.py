# 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
negative = -3
print(abs(negative))  # 3


# 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
empty_list = []
# bool() 함수를 통해 boolean 값 출력
# 빈 리스트는 False를 반환
print(bool(empty_list))  # False


# 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
my_list = [1, 2, 3, 4, 5]
# sum() 함수로 리스트의 모든 값 합산 출력
print(sum(my_list))  # 15


# 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
unsorted_list = ['하', '교', '캅', '의', '지', '가']
# sorted() 함수로 오름차순 정렬 후 출력 (가 -> 하)
# 원본 리스트를 변경하지 않고 정렬된 새 리스트를 반환
print(sorted(unsorted_list))  # ['가', '교', '의', '지', '캅', '하'] 