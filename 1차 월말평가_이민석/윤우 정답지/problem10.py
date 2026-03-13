    ############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def robot_simulation(commands):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result = [0,0,0] #(x,y, 방향) 방향 :  동 : 0 남: 1 서 : 2 북 : 3
    for i in commands: 
        if i == 'G': #동서남북 방향에 따라 직진하는 경우를 나눠서 x,y값계산
            if result[2] ==0: 
                result[0]+=1
            elif result[2]==1: 
                result[1]-=1
            elif result[2]==2:
                result[0]-=1
            else:
                result[1]+=1            
        elif i == 'B': #동서남북 방향에 따라서 후진하는 경우를 나눠서 x,y값계산
            if result[2] ==0:
                result[0]-=1
            elif result[2]==1: 
                result[1]+=1
            elif result[2]==2:
                result[0]+=1
            else:
                result[1]-=1
        elif i =='R': #동서남북 방향에 따라서 오른쪽 회전시 방향값을 변경
            if result[2]!=3:
                result[2]+=1
            else: 
                result[2]=0
        else :  #동서남북 방향에 따라서 왼쪽 회전시 방향값을 변경
            if result[2]!=0:
                result[2]-=1
            else: 
                result[2]=3
    result.pop(2) #방향 값 제거 
    result_1 = tuple(result) #tuple로 형변환
    return result_1
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
# 설명: 
# 1. 시작(0,0,동) -> G -> (1,0,동)
# 2. R회전 -> (남쪽을 봄)
# 3. G -> (1,-1,남)
# 4. L회전 -> (동쪽을 봄)
# 5. G -> (2,-1,동)
# 6. R회전 -> (남쪽을 봄)
# 7. G -> (2,-2,남)
print(robot_simulation("GRGLGRG"))  # 결과: (2, -2)
#####################################################