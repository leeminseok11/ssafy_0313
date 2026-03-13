n = int(input())
arr = list(map(int, input().split()))

min_value = arr[0]
max_value = arr[0]

for i in range(n):
    if min_value > arr[i]:
        min_value = arr[i]
    if max_value < arr[i]:
        max_value = arr[i]

print(f'{min_value} {max_value}')