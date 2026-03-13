n = int(input())
arr = list(map(int, input().split()))

max_value = arr[0]
for i in range(n):
    if max_value < arr[i]:
        max_value = arr[i]
total = 0
for j in range(n):
    arr[j] = arr[j]/max_value*100
    total += arr[j]
    a = total/n
print(f'{a:.6f}')