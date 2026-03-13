N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
# arr_1 = list(data_1)

for num in data_1:
    arr_1.append(num)
print(arr_1)

for i in range(N):
    arr_1.append(data_1[i])
print(arr_1)


M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
arr_2 = list(map(int, data_2.split()))
# print(arr_2)
# 1차원 배열 입력 받기
# arr = list(map(int, input().split()))
# print(arr)

for num in arr_2:
    if num % 2 == 1:  # 산술, 비교, 논리
        print(num)