def dfs(k):
    global lst

    if k == M:
        print(*lst)
        return

    for i in range(len(numLst)):
        lst.append(numLst[i])
        dfs(k+1)
        lst.pop()


N, M = map(int, input().split())
numLst = sorted(list((set(map(int, input().split())))))
lst = []
print(numLst)
dfs(0)






