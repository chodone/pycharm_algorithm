def find(i, lst):
    global maxV

    if i == N-1:
        maxV = max(maxV, sum(lst))
        return

    elif lst[-1] >= progLst[i + 1]:
        maxV = max(maxV, sum(lst))
        return

    for j in range(i+1, N):
        if progLst[j] > lst[-1]:
            lst.append(progLst[j])
            find(j, lst)
            lst.pop()



N = int(input())
progLst = list(map(int, input().split()))
Used = [False] * N
maxV = 0
partSumLst = []

for i in range(N):
    Used[i] = True
    partSumLst.append(progLst[i])
    find(i, partSumLst)
print(maxV)