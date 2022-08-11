
TC = int(input())

for tc in range(1, TC+1):
    forth_lst = list(input().split())
    stack = []

    for ele in forth_lst:
        if stack and ele == '+':  # 스택이 채워져 있고 더하기 일때
            if len(stack) < 2:
                print(f'#{tc} error')
                break
            else:
                newTop = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(newTop)


        elif stack and ele == '*':   # 스택이 채워져 있고 곱하기 일때
            if len(stack) < 2:
                print(f'#{tc} error')
                break
            else:
                newTop = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(newTop)

        elif stack and ele == '-':   # 스택이 채워져 있고 빼기 일때
            if len(stack) < 2:
                print(f'#{tc} error')
                break
            else:
                newTop = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(newTop)


        elif stack and ele == '/':   # 스택이 채워져 있고 나누기 일때
            if len(stack) < 2:
                print(f'#{tc} error')
                break
            else:
                newTop = stack[-2] // stack[-1]
                stack.pop()
                stack.pop()
                stack.append(newTop)

        elif ele == '.':
            if len(stack) != 1 or type(stack[0]) != int:
                print(f'#{tc} error')
                break

            else:
                print(f'#{tc} {stack[0]}')



        else:
            try:
                stack.append(int(ele))
            except ValueError:
                print(f'#{tc} error')
                break