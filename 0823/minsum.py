



def per(k, curS):


    if curS > minimum[0]:
        return

    if k == N:
        if curS < minimum[0]:
            minimum.pop()
            minimum.append(curS)
            return
        else:
            return



    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result[k] = i
            per(k+1, curS+mapp[k][result[k]]) #mapp[k][i]
            visited[i] = False




TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    mapp = [list(map(int, input().split())) for _ in range(N)]

    result = [-1] * N
    visited = [False] * N
    curSum = 0
    minimum = [100000]

    per(0, curSum)

    print(f'#{tc} {minimum[0]}')
