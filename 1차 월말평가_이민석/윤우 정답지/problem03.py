############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# 제한 Python 내장 함수: reversed, list.reverse
# 기본 점수 (9점): 제한 내장 함수를 사용하여 해결
# 가산점(+3점): 제한 내장 함수 없이 직접 구현 (총 12점)

def reverse_list(visited_items):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    list_1 = visited_items.copy() #같은 크기의 리스트를 복사 

    count = -1 # index값 설정
    for i in visited_items:
        count +=1 #index길이 측정
    for i in visited_items:
        list_1.pop(count) #리스트의 역순 배치를 위해 마지막 요소부터 제거 
        list_1.insert(count,i) # 마지막 요소부터 값 삽입 
        count-=1 # index값 감소하여 역순 설정
        
    return list_1
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
print(reverse_list(['A', 'B', 'C']))  # ['C', 'B', 'A']
#####################################################

