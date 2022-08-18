import sys
sys.stdin = open("input.txt", "r")

def find(data1, data2):
    start, end = 0, 99
    ST = []
    visited = [False] * 100

    ST.append(start)
    visited[start] = True

    while ST:
        v = ST.pop(-1)
        if v == 99:
            return 1
        else:
            if data1[v] and not visited[data1[v]]:
                ST.append(data1[v])
                visited[data1[v]] = True

            if data2[v] and not visited[data2[v]]:
                ST.append(data2[v])
                visited[data2[v]] = True
    return 0






TC = 10
for tc in range(1, TC+1):
    T, N = map(int, input().split())

    data1 = [0] * 100
    data2 = [0] * 100

    path_lst = list(map(int, input().split()))
    for idx in range(0,len(path_lst),2):
        if not data1[path_lst[idx]]:
            data1[path_lst[idx]] = path_lst[idx+1]
        else:
            data2[path_lst[idx]] = path_lst[idx+1]

    print(f'#{tc} {find(data1, data2)}')
