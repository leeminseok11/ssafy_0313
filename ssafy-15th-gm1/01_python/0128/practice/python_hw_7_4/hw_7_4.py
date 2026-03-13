'''사람의 이름과 나이를 입력받아 자신을 소개하는 Person 클래스를 작성하시오.
클래스에는 자신을 소개하는 introduce 인스턴스 메서드가 포함되어야 하고, 
인스턴스가 생성될 때 마다 증가하는 number_of_people 클래스 변수가 작성되어야 한다.'''

# 아래 클래스를 수정하시오.
class Person:
    # 클래스변수, 인스턴스가 생성될 때마다 증가
    number_of_people = 0 

    # 생성자, 인스턴스 생성시 자동 호출
    def __init__(self, name, age):
        self.name = name            # self.name 인스턴스 변수
        self.age = age
        Person.number_of_people += 1    # 인스턴스 생성시 마다 증가

    # 인스턴스 메소드
    def introduce(self):
        print(f'제 이름은 {self.name}이고, 저는 {self.age}살 입니다.')


person1 = Person("Alice", 25)  # 생성자
person1.introduce() # 인스턴스.메소드()
print(Person.number_of_people)

person2 = Person("Kim", 20)  # 생성자
person2.introduce() # 인스턴스.메소드()
print(Person.number_of_people)
