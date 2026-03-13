import sys; sys.stdin= open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    t=int(input())
    fx= input()


    stack = [0]*100
    top = -1
    icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
    isp = {'(':0, '*':2, '/':2, '+':1, '-':1}


    susik = ''
    for x in fx:
        if x  not in '(+-*/)':
            susik += x
        elif x ==')':
            while top>-1 and stack[top] != '(':
                top -= 1
                susik += stack[top+1]
            if top != -1:
                top -=1
        else:
            if top == -1 or isp[stack[top]] < icp[x]:
                top += 1
                stack[top] = x
            elif isp[stack[top]] >= icp[x]:
                while top > -1 and isp[stack[top]] >= icp[x]:
                    susik += stack[top]
                    top -= 1
                top += 1
                stack[top] = x

    while top > -1:
        top -= 1
        susik += stack[top +1]

    for x in susik:
        if x not in '+-/*':
            top += 1
            stack[top] =int(x)
        else:
            op2 = stack[top]
            top -= 1
            op1 = stack[top]
            top -= 1
            if x == '+':
                top += 1
                stack[top] = op1 + op2
            elif x == '-':
                top += 1
                stack[top] = op1 - op2
            elif x == '/':
                top += 1
                stack[top] = op1 / op2
            elif x == '*':
                top += 1
                stack[top] = op1 * op2
    print(f'#{tc} {stack[top]}')