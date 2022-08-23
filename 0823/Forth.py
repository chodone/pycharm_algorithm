

TC = int(input())

for tc in range(1, TC+1):

    line = list(input().split())
    ST = []

    for ele in line:
        if ele != '+' and ele != '-' and ele != '*' and ele != '/' and ele != '.':
            ST.append(int(ele))
        elif ele == '.':
            if len(ST) > 1 or type(ST[0]) != int:
                print(f'#{tc} error')
                break
            else:
                print(f'#{tc} {ST[0]}')


        else:
            if ele == '+' and len(ST) >= 2:
                a = ST.pop()
                b = ST.pop()
                ST.append(b + a)
            elif ele == '-' and len(ST) >= 2:
                a = ST.pop()
                b = ST.pop()
                ST.append(b - a )
            elif ele == '*' and len(ST) >= 2:
                a = ST.pop()
                b = ST.pop()
                ST.append(b * a)
            elif ele == '/' and len(ST) >= 2:
                a = ST.pop()
                b = ST.pop()
                ST.append(b // a)
            else:
                print(f'#{tc} error')
                break


