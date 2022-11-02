# 활주로
def load (lst):
    global cnt
    checkLoad = [lst.pop(0)]
    hLst = [True]

    while lst:
        if checkLoad[-1] == lst[0]:
            checkLoad.append(lst.pop(0))
            hLst.append(True)

        # 높이 1 감소
        elif checkLoad[-1] - lst[0] == 1:
            checkNum = lst[0]
            if len(lst) >= X:
                for i in range(X):
                    if lst[i] == checkNum:
                        checkLoad.append(lst[i])
                        hLst.append(False)
                    else:
                        return

                for k in range(X):
                    lst.pop(0)

            else:
                return




        # 높이 1 증가
        elif checkLoad[-1] - lst[0] == -1:
            checkNum = checkLoad[-1]
            if len(checkLoad) >= X:
                for j in range(-1, -X-1, -1):
                    if checkLoad[j] == checkNum and hLst[j]:
                        continue
                    else:
                        return
                checkLoad.append(lst.pop(0))
            else:
                return



        # 그 외의 경우의 수는 모두 return
        else:
            return

    cnt += 1

TC = int(input())
for tc in range(1, TC + 1):
    N, X = map(int, input().split())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0


    for row in range(N):
        rowLst = []
        for col in range(N):
            rowLst.append(Arr[row][col])
        load(rowLst)

    for col in range(N):
        colLst = []
        for row in range(N):
            colLst.append(Arr[row][col])
        load(colLst)

    print(f'#{tc} {cnt}')