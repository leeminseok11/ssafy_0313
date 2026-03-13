import sys; sys.stdin= open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    arr = input().split()
    stack = [0]* 100
    top = -1
    flag = True
    for token in arr:
        if token not in '+-/*.':
            top += 1
            stack[top] = int(token)

        elif token in '+-/*':
            if top <1:
                flag = False
                break
            op2 = stack[top]
            top -= 1
            op1 = stack[top]
            top -= 1

            if token == '+':
                top += 1
                stack[top] = op1 + op2
            elif token == '-':
                top += 1
                stack[top] = op1 - op2
            elif token == '*':
                top += 1
                stack[top] = op1 * op2
            elif token == '/':
                top += 1
                stack[top] = op1 // op2

        elif token == '.':
            break

    if flag == False or top != 0 :
        print(f'#{tc} error')
    else:
        print(f'#{tc} {stack[top]}')