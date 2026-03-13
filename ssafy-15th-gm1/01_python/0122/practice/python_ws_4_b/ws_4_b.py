food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.
# 1. for문
for food in food_list:
    if food['이름'] == '토마토':
        food['종류'] = '과일'
    elif food['이름'] == '자장면':
        print('자장면엔 고춧가루지')
    
    print(f"{food['이름']}  은/는 {food['종류']} (이)다.")        
print(food_list)

# 2. while
# 제어변수 초기화
# while 조건문:
#   할일
#   증감
i = 0
while i < len(food_list):
    if food['이름'] == '토마토':
        food['종류'] = '과일'
    elif food['이름'] == '자장면':
        print('자장면엔 고춧가루지')
    
    print(f"{food['이름']}  은/는 {food['종류']} (이)다.") 

    i += 1

print(food_list)