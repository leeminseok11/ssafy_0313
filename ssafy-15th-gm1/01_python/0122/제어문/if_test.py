# 점수를 받아서 수, 우, 미, 양, 가를 출력하시오.

score = int(input())
# 다중 분기문
if score >= 90:
    grade = '수'
elif score >= 80:
    grade = '우'
elif score >= 70:
    grade = '미'
elif score >= 60:
    grade = '양'
else:
    grade = '가'
print(grade)

