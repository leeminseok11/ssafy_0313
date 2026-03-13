import sys;
sys.stdin = open('반복문자지우기_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    text = input()
    stack = []
    for token in text:
        # 1. 스택이 비어 있거나 stack[-1] 값과 token이 다를 때 -> push
        if not stack or stack[-1] != token:
            stack.append(token)
        # elif stack[-1] == token:
        # 2. stack[-1] 값과 token이 같을 때
        else:
            stack.pop()

    print(f'#{tc} {len(stack)}')

