from pprint import pprint

TC = int(input())

def mySum(i, j, M):
    if 0 <= i+M <= N and 0 <= j+M <= N:
        sum = 0
        for k in range(i, i+M):
            for l in range(j , j+M):
                sum += mapp[k][l]
        return sum

    else:
        return 0




for tc in range(1, TC+1):
    N, M = map(int, input().split())

    mapp = [list(map(int, input().split())) for _ in range(N)]

    maxSum = 0
    for i in range(N-1):
        for j in range(N-1):
            res = mySum(i, j, M)

            if res > maxSum:
                maxSum = res

    print(f'#{tc} {maxSum}')
