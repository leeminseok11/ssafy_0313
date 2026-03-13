import sys
sys.stdin = open("회문1_input.txt")

def check(arr, col, row, length):
  cnt = 0   # 초기값 0으로 설정
  if arr[col][row] == arr[col][row + length - 1]: # 리스트의 처음과 마지막이 같다면
      n_arr = arr[col][row: row + length]
      if arr[col][row: row + length] == n_arr[::-1]: # 리스트의 내용이 같다면
          cnt += 1

  return cnt


T = 10
for tc in range(1, T+1):
  M = int(input()) # 범위 설정
  arr = [list(map(str, input())) for _ in range(8)]
  N = len(arr)
  trans_arr = list(map(list, zip(*arr))) # 전치행렬 생성
  result = 0

  for i in range(N):
      for j in range(N-M+1):# 행은, 범위를 제한
          result += check(arr, i, j, M) # 행렬에서 회문 확인
          result += check(trans_arr, i, j, M) # 전치행렬에서 회문 확인
  print(f'#{tc} {result}')
