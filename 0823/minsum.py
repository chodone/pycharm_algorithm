
TC = int(input())

for i in range(1, TC+1):
    N = int(input())

    mapp = [list(map(int, input().split())) for _ in range(N)]

    print(mapp)