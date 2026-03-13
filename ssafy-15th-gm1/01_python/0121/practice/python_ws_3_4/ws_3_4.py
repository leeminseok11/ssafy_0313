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


number_of_people = 0
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# print(list(map(create_user, name, age, address)))
users = []
for i in range(len(name)):
    users.append(create_user(name[i], age[i], address[i]))

print(users)
