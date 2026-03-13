number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    increase_user()
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address

    print(f'{name}님 환영합니다!')
    return user_info

users = list(map(create_user, name, age, address))

many_user = None


number_of_book = 100

def decrease_book(number):
    global number_of_book
    number_of_book -= number

    print(f'남은 책의 수 : {number_of_book}')

 
#def rental_book(name, number):
#    decrease_book(number)
#    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

def rental_book(info):
    name = info['name']
    age = info['age']

    rent_count = age // 10
    decrease_book(rent_count)
    print(f'{name}님이 {rent_count}권의 책을 대여하였습니다.')


many_user = []
for user in users:
    many_user.append({user['name']: user['age']})


for info in users:
    rental_book(info)