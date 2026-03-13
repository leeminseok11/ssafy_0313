import sys; sys.stdin = open('stack_1.txt')

T = int(input())

for tc in range(1, T + 1):
    s = input().strip()
    stack = []

    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    print(f"#{tc} {len(stack)}")
