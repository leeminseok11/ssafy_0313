number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1
    


def create_user(name, age, addr):
    increase_user()
    data = {
        '이름': name,
        '나이': age,
        '주소': addr,
    }
    print(f'{name}님 환영합니다!')
    return data

print(f'현재 가입 된 유저수 : {number_of_people}')
print(create_user('홍길동', 30, '서울'))
print(f'현재 가입 된 유저수 : {number_of_people}')

