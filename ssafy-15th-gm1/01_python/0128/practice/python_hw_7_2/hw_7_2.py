# 아래 클래스를 수정하시오.
class StringRepeater:  
    def repeat_string(self, num, text):
        for _ in range(num):
            print(text)

# 기본생성자는 클래스에 정의 하지 않음
repeater1 = StringRepeater()  # 생성자
repeater1.repeat_string(3, "Hello") # 메소드


# 스네이크 케이스 : num_of_student , 파이썬, C
# 카멜케이스 : numOfStudent, Java
# 파스칼 케이스 : NumOfStudent, class 정의
# 케밥 케이스 : num-of-student, 웹