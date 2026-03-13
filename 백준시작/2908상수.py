n, m = input().split()

N = int(n[::-1])
M = int(m[::-1])

if N > M :
    print(N)
else:
    print(M)