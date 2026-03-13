matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.

# matrix의 전체 길이를 구하기(len 사용X)
# 전체 길이를 저장할 변수
matrix_len = 0
for row in matrix:
    # 각 리스트를 하나씩 셀 때마다 +1
    matrix_len += 1

print(matrix_len)

# 각 요소(행)의 길이 구하기(len 사용X)
for number in matrix:
    temp_len = 0
    # 리스트 내부 요소의 갯수 세기
    for _ in number:
        temp_len += 1
    # 개수가 4개 이하인 경우에만 출력
    if temp_len <= 4:
        print(f'{number} 리스트는 {temp_len}개 만큼 요소를 가지고 있습니다.')

# range와 len 사용하여 인덱스 기반 접근 및 출력
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f'matrix dml {i}, {j}번째 요소의 값은 {matrix[i][j]}입니다.')