import sys;sys.stdin = open('괄호검사_input.txt')

def solve(text):
    stack = []
    for token in text:
        # 1. 왼쪽괄호 -> push
        if token == '(' or token == '{': # token in '({'
            stack.append(token)
        # 2. 오른쪽괄호 -> pop
        elif token == ')' or token == '}':
            # 2.1. isEmpty  -> return False
            if not stack: # len(stack) == 0
                return 0
            else:
                # 2.2. tmp = pop()
                tmp = stack.pop()
                # 2.2.1. 짝검사 -> return false
                if token == ')' and tmp != '(':
                    return 0
                elif token == '}' and tmp != '{':
                    return 0

    # 3. if stack : return False
    if stack : return 0
    # 1~3를 통과한 경우 :return True
    return 1

T = int(input())
for tc in range(1, T+1):
    text = input()
    print(f'#{tc} {solve(text)}')