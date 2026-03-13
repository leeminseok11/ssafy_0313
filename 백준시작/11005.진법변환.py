n, m = map(int, input().split())
mapping = {}
for i in range(10, 36):
    mapping[i] = chr(i+55)

result = []
while n > 0:
    a = n % m
    if a >= 10:
        a = mapping[a]
    else:
        a = str(a)
    result.append(a)
    n = n//m

result.reverse()
print(''.join(result))
