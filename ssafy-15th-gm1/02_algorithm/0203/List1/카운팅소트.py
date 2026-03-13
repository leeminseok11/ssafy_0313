def counting_sort(data, result, k): # 원본, 출력, 최대값
    # 1. 카운팅
    cnts = [0] * k
    for i in range(N):
        cnts[data[i]] += 1
    # 2. 누적
    for i in range(1, k):  # 1 4 5 6 8
        cnts[i] += cnts[i-1]
    # 3. 자리배치
    for i in range(N-1, -1, -1):
        cnts[data[i]] -= 1
        result[cnts[data[i]]] = data[i]
    # 참조형변수는 리턴하지 않는다.

data = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(data)
result = [0] * N
counting_sort(data, result, max(data)+1)
print(result)