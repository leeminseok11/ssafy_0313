def increase_user():
    global number_of_people
    number_of_people += 1
    

def create_user(name, age, addr):
    increase_user()
    data = {
        'name': name,
        'age': age,
        'address': addr,
    }
    print(f'{name}님 환영합니다!')
    return data


def decrease_book(num):
    global number_of_book
    number_of_book -= num
    print(f'남은 책의 수 : {number_of_book}')


def rental_book(info):
    for key, value in info.items():
        us_name = key
        us_age = value
    decrease_book(us_age // 10)
    print(f'{us_name}님이 {us_age // 10}권의 책을 대여하였습니다.')


number_of_people = 0
number_of_book = 100
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# 4번 문제에서 사용한 코드 이용
many_user = list(map(create_user, name, age, address))   
# print(many_user)

# 4번 문제의 결과를 활용하여 모든 고객 정보를 순회하며 {이름: 나이} 딕셔너리 생성
user_info = []                                            
for user in many_user:
    info_dict = {user['name']: user['age']}
    user_info.append(info_dict)

print(f'전체 회원 수는 : {number_of_people}명')

# 각 고객에 대해 rental_book() 함수 실행
for info in user_info:
    rental_book(info)
