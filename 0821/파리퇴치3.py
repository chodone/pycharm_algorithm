def x_spray(i, j):
    sum = mapp[i][j]

    for k in range(1,M):
        for l in range(i-k, i+k+1, 2*k):
            for g in range(j-k, j+k+1, 2*k):
                if 0 <= l < N and 0 <= g < N:
                    sum += mapp[l][g]
    return sum



def plus_spray(i, j):
    sum = -mapp[i][j]

    for k in range(i-M+1, i+M):
        if 0 <= k < N:
            sum += mapp[k][j]
    for l in range(j-M+1, j+M):
        if 0 <= l < N:
            sum += mapp[i][l]

    return sum





TC = int(input())

for tc in range(1, TC + 1):
    N , M = map(int, input().split())

    mapp = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    for i in range(N):
        for j in range(N):
            x = x_spray(i,j)
            plus = plus_spray(i, j)

            if res < x:
                res = x
            if res < plus:
                res = plus

    print(f'#{tc} {res}')
