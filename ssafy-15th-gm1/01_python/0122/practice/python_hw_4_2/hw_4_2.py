list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    # '난중일기',
    '홍길동전',
    '만복자서포기',
]

# 두개의 리스트를 비교하기 위해서는 2중 for가 필요
# for문 실행 후에 for문이 정상적으로 종료 또는 break로 종료되었는지를 구분하기 위해서 flag 변수 사용

# 1. 2중 for문과  flag 변수를 사용

for rental in rental_list:
    flag = False    # 대여 불가능
    for book in list_of_book:
        if rental == book:
            flag = True # 대여 가능
            break
    if not flag:  # flag == False   
        print(f'{rental} 은/는 보유하고 있지 않습니다.')
        break
if flag:
    print('모든 도서가 대여 가능한 상태입니다.')

# 2. for + in + flag
for rental in rental_list:
    # for문을 대신 해서 in를 사용
    flag = True   # 대여 가능
    if rental not in list_of_book:
        print(f'{rental} 은/는 보유하고 있지 않습니다.')
        flag = False   # 대여 불가능
        break
if flag:
    print('모든 도서가 대여 가능한 상태입니다.')

# for ~ else
for rental in rental_list:
    # for문 대신 in 를 사용
    if rental not in list_of_book:
        print(f'{rental} 은/는 보유하고 있지 않습니다.')
        break
else: # for문이 정상적으로 종료(break에 안 걸렸을 때)
   print('모든 도서가 대여 가능한 상태입니다.') 