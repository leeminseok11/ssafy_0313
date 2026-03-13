title = '딕셔너리 활용하기'

# 딕셔너리를 선언하면서 key-value쌍을 할당
data = {
    '과목': 'Python',
    '구분': '실습',
    '단계': 2,
    '문제번호': 3251,
    '이름': None,
    '일차': 22,
}
print(data)

# 딕셔너리 항목 수정 : 기존 키값이 있으면
data['단계'] = str(data['단계']) + '단계'
data['이름'] = title
# data['일차'] = data['일차'] - 20
data['일차'] -= 20
print(data)

# 딕셔너리 항목 추가 : 기존 키값이 없으면
data['날짜'] = '2026-01-21'
print(data)

# 딕셔너리에서 없는 키값을 출력하면 ???
# print(data['점심'])   # Key Error
print(data.get('점심'))

#  1 증가시키는 방법
a = 1
a = a + 1
a += 1
# a++