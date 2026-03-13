############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 반드시 재귀 함수 형태로 구현해야 합니다.
def categorize_books(books):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result ={} # 결과값 생성
    for i in books: 
            if i['category'] not in result: #결과값의 key 값에 없으면 생성후 key, value값 추가 
                result[i['category']] = [i['title']]
            else:
                result[i['category']].append(i['title']) # 결과값의 key 값에 있을 시 value만 추가 
            
    return result
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
books_data = [
    {'title': 'Python Basic', 'category': 'IT'},
    {'title': 'Java Standard', 'category': 'IT'},
    {'title': 'History of World', 'category': 'History'},
    {'title': 'Cooking 101', 'category': 'Life'}
]
# 결과:
# {
#   'IT': ['Python Basic', 'Java Standard'],
#   'History': ['History of World'],
#   'Life': ['Cooking 101']
# }
print(categorize_books(books_data))
#####################################################