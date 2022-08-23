def par(k, curSum):

    if curSum > 10: #현재 합이 10 이상이면 밑으로 더이상가지 마라 백트랙킹
        return

    if k == N:
        #print(result)
        # sumV = 0
        # for i in range(N):
        #     if result[i] == 1:
        #         sumV += lst[i]
        if curSum == 10:
            for i in range(N):
                if result[i] == 1:
                    print(lst[i], end=' ')
            print()

    else:
        result[k] = 0
        par(k+1, curSum)

        result[k] = 1
        par(k+1, curSum+lst[k])

lst = [1,2,3,4,5,6,7,8,9,10]
N = 10
result = [-1] * N
par(0,0)







