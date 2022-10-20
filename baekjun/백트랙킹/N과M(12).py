def dfs(k,preNum):
    if k == M:
        print(*lst)

        return

    for i in range(len(numLst)):
        if preNum <= numLst[i]:
            lst.append(numLst[i])
            dfs(k+1, numLst[i])
            lst.pop()





N, M = map(int, input().split())
numLst = sorted(list(set(map(int, input().split()))))
lst = []

dfs(0, 0)