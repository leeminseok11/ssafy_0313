def enq(n):
    global last
    last += 1
    heap[last] = n

    c = last
    p = c // 2

    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2
import sys
sys.stdin = open('이진힙.txt')

T = int(input())
for tc in range(1, T+1):

    n = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (n + 1)
    last = 0
    for i in arr:
        enq(i)
    result = 0
    x = last // 2
    while x > 0:
        result += heap[x]
        x //= 2
    print(f"#{tc} {result}")
