def perm(k,midSum):
    global minV
    if k == change:
        if midSum < minV:
            minV = midSum

        return

    if midSum > minV:
        return

    for i in range(len(numArr)):
        for j in range(i+1, len(numArr)):
            numArr[i], numArr[j] = numArr[j], numArr[i]

            for k in range(N):

            perm(k+1, )







TC = int(input())

for tc in range(1, TC + 1):
    numArr, change = input().split()
    numArr = list(map(int, numArr))
    N = len(numArr)
    change = int(change)
    minV = 1e10



    print(numArr, change)
