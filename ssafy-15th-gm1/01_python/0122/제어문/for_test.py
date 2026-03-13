# 1 ~ 10 까지의 합을 구하시오.
# 1 ~ 10 까지의 짝수합을 구하시오.
# 1 ~ 10 까지의 홀수합을 구하시오.
# 단, for문은 한번만 사용한다.
# 힌트, 합변수(total), 짝합(even_total), 홀수(odd_total) 선언 위치를 주의

total = 0
even_total = 0
odd_total = 0
for i in range(1, 11):
    total += i
    if i % 2 == 0:
        even_total += i
    else:
        odd_total += i
print(total)
print(even_total)
print(odd_total)

###############################
# 2중 for문을 이용하여  구구단을 작성하시오.
# 2단
# 2 X 1 = 2
# 2 X 2 = 4
# 2 X 3 = 6
# ...
# 2 X 9 = 18
# 3단
# ...

for i in range(2, 10):
    print(f'{i}단')
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j}')