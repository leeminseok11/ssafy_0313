import sys; sys.stdin = open('stack_1.txt')

T = int(input())

for tc in range(1, T + 1):
    s = input().strip()
    stack = []
    a = 1

    for i in s:
        if i == '(' or i == '{':
            stack.append(i)

        elif i == ')':
            if not stack or stack[-1] != '(':
                a = 0
                break
            stack.pop()

        elif i == '}':
            if not stack or stack[-1] != '{':
                a = 0
                break
            stack.pop()
    if stack:
        a = 0

    print(f"#{tc} {a}")