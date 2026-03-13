import  sys;sys.stdin = open('Forth_input.txt')
def forth(text):
    stack = []
    for tok in text:
        # 숫자
        if tok not in '+-*/.': # tok.isdigit()
            stack.append(tok)
        # 연산자
        elif tok in '+-*/':
            # 스택에 두개 이상 숫자가 있어야 함
            if len(stack) >= 2:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if tok == '+':
                    stack.append(op1 + op2)
                elif tok == '-':
                    stack.append(op1 - op2)
                if tok == '*':
                    stack.append(op1 * op2)
                if tok == '/':
                    stack.append(op1 // op2)
            else:
                return 'error'
        # 점(.)
        elif tok == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'


T = int(input())
for tc in range(1, T+1):
    text = list(map(str, input().split()))
    print(f'#{tc} {forth(text)}')