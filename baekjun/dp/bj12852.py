import copy


def makeOne(k, curN):
    global minV
    global res


    if curN == 1:

        if minV > k:
            minV = k
            res = copy.deepcopy(divLst)
        return

    elif minV < k:
        return


    if curN % 3 == 0 and curN % 2 == 0:
        divLst.append(curN//3)
        makeOne(k+1, curN//3)
        divLst.pop()

        divLst.append(curN//2)
        makeOne(k+1, curN//2)
        divLst.pop()

        divLst.append(curN - 1)
        makeOne(k+1, curN-1)
        divLst.pop()

    elif curN % 3 == 0:
        divLst.append(curN//3)
        makeOne(k+1, curN//3)
        divLst.pop()

        divLst.append(curN-1)
        makeOne(k+1, curN-1)
        divLst.pop()

    elif curN % 2 == 0:

        divLst.append(curN // 2)
        makeOne(k + 1, curN // 2)
        divLst.pop()

        divLst.append(curN-1)
        makeOne(k+1, curN-1)
        divLst.pop()

    else:
        divLst.append(curN - 1)
        makeOne(k + 1, curN - 1)
        divLst.pop()


N = int(input())
minV = 1e10
divLst = []
res = []
divLst.append(N)

makeOne(0, N)

print(minV)
print(*res)