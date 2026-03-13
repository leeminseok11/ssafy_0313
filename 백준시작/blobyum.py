n, k = map(int, input().split())
a = list(map(int, input().split()))

a = a*2

sum_k = sum(a[0:k])
max_k = sum_k
for i in range(1, n):
    sum_k = sum_k - a[i-1] + a[i+k-1]
    max_k = max(sum_k, max_k)

print(max_k)



