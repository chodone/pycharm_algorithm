def inorder(root):
    if root != 0:
        inorder(tree[root][0])
        print(nodeLst[root], end='')
        inorder(tree[root][1])




TC = 10

for tc in range(1, TC + 1):
    N = int(input())

    nodeLst = [0]
    nodeLine = []

    for i in range(N):
        lst = list(input().split())
        if len(lst) == 4:
            nodeLst.append(lst[1])
            for j in range(2, 4):
                nodeLine.append(int(lst[0]))
                nodeLine.append(int(lst[j]))
        elif len(lst) == 3:
            nodeLst.append(lst[1])
            nodeLine.append(int(lst[0]))
            nodeLine.append(int(lst[2]))
        else:
            nodeLst.append(lst[1])

    tree = [[0,0] for _ in range(N+1)]

    for i in range(0, len(nodeLine), 2):
        p, c = nodeLine[i], nodeLine[i + 1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c



    print(f'#{tc}', end = ' ')
    inorder(1)
    print()





