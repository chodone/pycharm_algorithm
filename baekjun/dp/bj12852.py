def makeOne(k, curN):
    global minV
    if curN == 1:
        min(minV, k)
        return

    if k > minV:
        return

    if curN % 3 == 0 and curN % 2 == 0:

        curN = curN // 3
        calLst.append(curN)
        makeOne(k+1, curN)
        calLst.pop()
        curN = curN * 3

        curN = curN // 2
        calLst.append(curN)
        makeOne(k+1, curN)

    elif curN % 3 == 0:
        curN = curN // 3
        calLst.append(curN)
        makeOne(k + 1, curN)

    elif curN % 2 == 0:
        curN = curN // 2
        calLst.append(curN)
        makeOne(k + 1, curN)

    else:
        curN -= 1
        calLst.append(curN)
        makeOne(k + 1, curN)



N = int(input())
calLst = []
calLst.append(N)
minV = 1e10

makeOne(0, N)
print(minV)