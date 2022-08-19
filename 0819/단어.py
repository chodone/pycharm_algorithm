def find(mapp, K):

    res = 0
    for line in mapp:
        cnt = 0
        for i in line:
            if i:
                cnt += 1
            if cnt == K+1 and i == 1:
                cnt = 0
            if cnt == K and i == 0:
                res += 1
                cnt = 0
            if cnt < K and i == 0:
                cnt = 0




        if cnt == K:
            res += 1

    return res





TC = int(input())

for tc in range(1, TC+1):

    N, K = map(int, input().split())

    mapp = [list(map(int, input().split())) for _ in range(N)]

    cMapp = []
    for i in range(N):
        column = []
        for j in range(N):
            column.append(mapp[j][i])
        cMapp.append(column)

    result = 0

    result = find(mapp, K) + find(cMapp, K)

    print(f'#{tc} {result}')
