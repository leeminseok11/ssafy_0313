def rental_book(name, num):
    decrease_book(num)
    print(f'{name}님이 {num}권의 책을 대여')


def decrease_book(num):
    global number_of_book
    number_of_book -= num
    print(f'남은 책의 수 : {number_of_book}')


number_of_book = 100
rental_book('홍길동', 3)