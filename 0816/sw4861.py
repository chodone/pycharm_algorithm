from pprint import pprint
TC = int(input())

for tc in range(1, TC+1):

    N, M = map(int, input().split())

    mapp = [input() for _ in range(N)]

    # pprint(mapp)

    findP = False

    for row in mapp:
        start = 0
        m = M
        while N - m >= 0:
            if row[start:m] == row[m-N-1:-N+start-1:-1]:
                print(f'#{tc} {row[start:m]}')
                findP = True
            start += 1
            m += 1
        if findP:
            break

    if not findP:
        for i in range(N):
            column = ''
            for j in range(N):
                column += mapp[j][i]
            # print(column)
            m = M
            start = 0
            while N - m >= 0:
                if column[start:m] == column[m-N-1:-N+start-1:-1]:
                    print(f'#{tc} {column[start:m]}')
                    findP = True
                start += 1
                m += 1
            if findP:
                break












