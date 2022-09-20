def function(idx, sumV):
    global minV
    # 모든 곳을 방문한 경우 (출발지로 돌아온 경우)
    if 0 not in visited:
    	# 최소 소비량 갱신
        if minV > sumV:
            minV = sumV
        return
    # 아직 방문 중인데, 소비량이 최소값을 넘어간 경우 return
    elif minV < sumV:
        return
    for i in range(N):
    	# i : 방문할 곳
        if i == idx:
            continue	# 현재위치로는 방문하지 않는다.
        if visited[i]:
            continue	# 이미 방문한 곳은 방문하지 않는다.
        if i == 0 and 0 in visited[1:]:
            continue	# 아직 방문하지 않은 곳이 있으면 출발지로 가지 않는다.
        visited[i] = True
        function(i, sumV + arr[idx][i])
        visited[i] = True


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    minV = 100000000
    function(0, 0)

    print(f'#{tc} {minV}')