def per(k):
    if k == N:
        # print(result)
        for i in range(N):
            print(lst[result[i]], end=' ')
        print()
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True  # 함수 호출하기전에 해줘야한다
            result[k] = i
            per(k+1)
            visited[i] = False # 원복시키기??





lst = [10, 20, 30]
N = 3
result = [-1] * N
visited = [False] * N
per(0)