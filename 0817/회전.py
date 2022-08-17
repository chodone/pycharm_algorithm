





TC = int(input())


for tc in range(1, TC+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    M %= N
    print(f'#{tc} {queue[M]}')








