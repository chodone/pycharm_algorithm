def find(lst):
    start, end = lst[0], lst[1]
    ST = []
    ST.append(start)



    while ST:
        for path in path_lst:
            if ST[0] == path[0]:
                ST.append(path[1])

        if ST[0] == end:
            return 1

        ST.pop(0)


    return 0






TC = int(input())

for tc in range(1, TC+1):
    V, E = map(int, input().split())

    path_lst = []
    for i in range(E):
        path_lst.append(list(map(int, input(). split())))



    print(f'#{tc} {find(list(map(int, input().split())))}')
