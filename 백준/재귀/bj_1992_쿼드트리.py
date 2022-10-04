def rec(k, flag, sr, sc):
    global res
    if k == 1:
        res += str(Arr[sr][sc])
        return

    for row in range(k):
        for col in range(k):
            if Arr[sr+row][sc+col] == flag:continue
            res += '('
            for i in range(0, k, k//2):
                for j in range(0, k, k//2):
                    rec(k//2, Arr[sr+i][sc+j], sr+i, sc+j)
            res += ')'
            return

    res += str(flag)



N = int(input())
Arr = [list(map(int, input())) for _ in range(N)]
res = ''

rec(N, Arr[0][0], 0, 0)
print(res)
