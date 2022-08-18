
TC = int(input())


for tc in range(1, TC+1):
    test_lst = input()
    stack_lst = []  # 여는 괄호가 나오면 담을 stack_lst

    for ele in test_lst:
        # 여는 괄호
        if ele == '(' or ele == '{':
            stack_lst.append(ele)

        # 닫는 괄호
        elif ele == ')':
            if not stack_lst or stack_lst[-1] != '(':
                print(f'#{tc} 0')
                break
            else:
                stack_lst.pop()
        elif ele == '}':
            if not stack_lst or stack_lst[-1] != '{':
                print(f'#{tc} 0')
                break
            else:
                stack_lst.pop()


        # 다른 문자
        else:
            continue
    else:
        if not stack_lst:
            print(f'#{tc} 1')

        else:
            print(f'#{tc} 0')