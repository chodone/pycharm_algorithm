def dfs(a):
    global cnt
    if a == rep:
        cnt += 1

        print(*sorted(s))

        return

    for i in range(len(s)-1, -1, -1):
        if not Used[i]:
            memory.append(s.pop(i))
            Used[i] = True
            dfs(a+1)
            s.append(memory.pop())
            Used[i] = False




while True:
    lst = list(map(int, input().split()))
    k = lst[0]
    s = lst[1:]
    rep = k - 6
    Used = [False] * len(s)
    memory = []

    if k == 0:
        break

    dfs(0)
    print(cnt)



