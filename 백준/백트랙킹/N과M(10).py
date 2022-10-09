# def seq(k,preNum, curNum, midSeq):
#
#
#     if preNum > curNum:
#
#         return
#
#     if k == M:
#         midSeq = int(midSeq)
#         if midSeq not in res:
#             res.append(midSeq)
#
#         return
#
#
#
#
#     for i in range(N):
#         if not Used[i]:
#             Used[i] = True
#             seq(k+1, curNum, numLst[i], midSeq+str(numLst[i]))
#             Used[i] = False
#
#
#
#
#
#
#
#
# N, M = map(int, input().split())
# numLst = list(map(int, input().split()))
# Used = [False] * N
#
# res = []
# for i in range(N):
#     Used[i] = True
#     seq(1, 0, numLst[i], str(numLst[i]))
#     Used[i] = False
#
# res.sort()
#
# for sq in res:
#     sq = str(sq)
#     for j in sq:
#         print(int(j), end=' ')
#     print()


#### 병시나아아아아아아아아 소팅을 하면 자동으로 내림차순이 된다는걸 왜 생각을 못해서 2시간동안이나 헤매고 앉아 있냐 이 뷰우우우우웅신


def dfs(start):
    if len(temp) == m:
        print(*temp)
        return

    remember_me = 0


    for i in range(start, n):
        if not visited[i] and remember_me != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            remember_me = nums[i]
            dfs(i + 1)
            visited[i] = False
            temp.pop()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []


dfs(0)

