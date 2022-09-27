
def calPrice(row, col):
    Visited[row]


TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())

    Arr = [list(map(int, input().split())) for _ in range(N)]
    Visited = [False] * N

    for product in range(N):
        for factory in range(N):
            calPrice(product, factory)

