from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")

def palind(row):

    N = 100
    M = 100

    while N - M < 100:

        start = 0
        m = M
        while N - m >= 0:
            if row[start:m] == row[m-N-1:start-N-1:-1]:
                return M
            m += 1
            start += 1
        M -= 1

    return 0




TC = 10

for tc in range(1, TC+1):
    n = int(input())

    mapp = [input()for _ in range(100)]

    MaxLen = 0

    for row in mapp:
        if MaxLen < palind(row):
            MaxLen = palind(row)

    for i in range(100):
        column = ''
        for j in range(100):
            column += mapp[j][i]
        if MaxLen < palind(column):
            MaxLen = palind(column)

    print(f'#{tc} {MaxLen}')


