def re(k, midS):
    if k == N-1:
        lst.append(midS)
        return

    if op[0]:
        op[0] -= 1
        re(k+1, midS + numberLst[k+1])
        op[0] += 1

    if op[1]:
        op[1] -= 1
        re(k+1, midS - numberLst[k+1])
        op[1] += 1

    if op[2]:
        op[2] -= 1
        re(k+1, midS * numberLst[k+1])
        op[2] += 1

    if op[3]:
        op[3] -= 1
        # if midS // numberLst[k+1] >= 0:
        #     re(k+1, midS // numberLst[k + 1])
        # else:
        #     re(k + 1, (midS // numberLst[k + 1]) + 1)
        re(k+1, int(midS / numberLst[k+1]))
        op[3] += 1


TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    op = list(map(int, input().split()))
    numberLst = list(map(int,input().split()))
    lst = []

    re(0, numberLst[0])

    res = max(lst) - min(lst)
    print(f'#{tc} {res}')

