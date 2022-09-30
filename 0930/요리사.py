
#
# def combi(k, s):
#     global minV
#     if k == N//2:
#         if k == N//2:
#             t = abs(calc(aList) - calc(bList))
#             if minV > t:
#                 minV = t
#
#             return
#
#     for i in range(s, N-r+k):
#         aList[k] = i
#         combi(k+1, i+1)





def calc(al, bl):
    A, B = 0, 0

    for i in range(len(al)):
        for j in range(i+1, len(al)):
            A += Arr[al[i]][al[j]] + Arr[al[j]][al[i]]

    for k in range(len(bl)):
        for l in range(k+1, len(bl)):
            B += Arr[bl[k]][bl[l]] + Arr[bl[l]][bl[k]]

    return abs(A - B)


def rec(k, aList, bList):
    global minV
    if k == N:
        if len(aList) == len(bList):
            t = calc(aList, bList)
            if minV > t:
                minV = t
        return


    rec(k+1, aList +[k], bList)
    rec(k+1, aList, bList +[k])









TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())

    Arr = [list(map(int, input().split())) for _ in range(N)]
    aList = []
    bList = []
    minV = 1e10
    # combi(0)
    rec(0, [], [])

    print(f'#{tc} {minV}')