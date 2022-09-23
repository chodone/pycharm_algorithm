def find(k, midSum):
    global res



    if k == N:
        if res > midSum >= B:
            res = midSum
        return

    if midSum >= res:
        return


    if not Visited[k]:
        Visited[k] = True
        find(k+1, midSum + crewLst[k])
        Visited[k] = False
        find(k+1, midSum)






TC = int(input())

for tc in range(1, TC + 1):
    N, B = map(int, input().split())
    crewLst = list(map(int, input().split()))
    Visited = [False] * N

    res = 1e10
    find(0,0)



    print(f'#{tc} {res- B}')


