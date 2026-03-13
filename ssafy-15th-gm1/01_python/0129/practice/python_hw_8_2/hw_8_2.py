# 아래 함수를 수정하시오.
def check_number():
    # 잘못된 입력 시(예: 문자열) 재시도를 안내하고
    # 올바른 입력(숫자)까지 반복

    # 올바른 입력이 들어올 때까지 무한 루프
    while True:
        try:
            # 사용자 입력
            # input()은 항상 문자열을 반환이므로  int()로 정수형을 반환
            num = int(input('숫자를 입력하세요 : '))

            # 입력된 숫자가 양수, 음수, 0인지 판별
            if num > 0:
                print('양수입니다.')
            elif num < 0:
                print('음수입니다.')
            else:
                print('0입니다.')
            #올바른 숫자가 입력되고 처리된 루프 종료
            break 
        # int(input())변환 과정에서 숫자가 아닌 값이 입력된 경우
        except :
            print('잘못된 입력입니다.')

check_number()
