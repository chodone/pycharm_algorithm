def rec(k, flag, sr, sc):
    if k == 1:
        cntLst[Arr[sr][sc]] += 1
        return

    for row in range(k):
        for col in range(k):
            if Arr[sr + row][sc + col] == flag : continue
            for i in range(0, k, k//3):
                for j in range(0, k, k//3):
                    rec(k//3, Arr[sr + i][sc + j], sr+i, sc+j)
            return

    cntLst[flag] += 1


N = int(input())

Arr = [list(map(int, input().split())) for _ in range(N)]
cntLst = [0, 0, 0]
rec(N, Arr[0][0], 0, 0)


print(f'{cntLst[-1]} \n{cntLst[0]} \n{cntLst[1]}')

