def find_set(x):
    while x != lst[x]:
        x = lst[x]

    return x


TC = int(input())

for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    lst = [k for k in range(N+1)]
    count = 0

    memoLst = list(map(int, input().split()))
    for i in range(M):
        n1 = find_set(memoLst[i*2])
        n2 = find_set(memoLst[i*2+1])
        lst[n2] = n1

    for i in range(1, N+1):
        if i == lst[i]:
            count += 1




    print(f'#{tc} {count}')


