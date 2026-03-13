import sys
sys.stdin = open('2to10.txt')

T = int(input())
for tc in range(1, T+1):
    arr = input().strip()
    result = []

    for i in range(0, len(arr), 7):
        a= arr[i:i+7]
        b= 0

        for j in range(7):
            b = b*2 + int(a[j])

        result.append(b)

    print(f'#{tc}', *result)
