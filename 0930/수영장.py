
def rec(k, midS):
    global minV
    if k >= 12:
        if midS < minV:
            minV = midS
        return


    elif midS > minV:
        return


    if plan[k]:

        # 일비용 월비용
        rec(k+1, midS + min(price[0]*plan[k], price[1]))
        rec(k+3, midS + price[2])
        rec(k+12, midS + price[3])
    else:
        rec(k+1,midS)






TC = int(input())

for tc in range(1, TC + 1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    minV = 1e10


    rec(0, 0)

    print(f'#{tc} {minV}')

