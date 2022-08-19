

def check(lst):
    check = [0] * 10

    for i in range(len(lst)):
        if check[lst[i]]:
            return 0
        else:
            check[lst[i]] = 1
    return 1



TC = int(input())

for tc in range(1, TC+1):

    mapp = [list(map(int, input().split())) for _ in range(9)]

    cMapp = []

    for i in range(9):
        column = []
        for j in range(9):
            column.append(mapp[j][i])
        cMapp.append(column)

    squareMapp = []

    for k in range(0, 9, 3):
        for i in range(0,9,3):
            square = []
            for l in range(k, k+3):
                for j in range(i , i+3):
                    square.append(mapp[j][l])

            squareMapp.append(square)




    for i in range(9):
        if check(mapp[i]) and check(cMapp[i]) and check(squareMapp[i]):
            continue
        else:
            print(f'#{tc} 0')
            break

    else:
        print(f'#{tc} 1')



