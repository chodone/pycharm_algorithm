def pre(root):
    if root != 0:
        print(root)
        pre(tree[root][0])
        pre(tree[root][1])



def pre1(root):
    print(root)
    if tree[root][0] != 0:
        pre(tree[root][0])
    if tree[root][1] != 0:
        pre(tree[root][1])


def inorder(root):
    if root != 0:
        inorder(tree[root][0])
        print(root)
        inorder(tree[root][1])

def postorder(root):
    if root != 0:
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root)







inputS = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'

lst = list(map(int, inputS.split()))
V = 13

tree = [[0, 0] for _ in range(V+1)]
parent = [0] * (V+1)
for idx in range(0, len(lst), 2):
    p, c = lst[idx], lst[idx + 1]
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    parent[c] = p
# print(tree)
pre(1)

# postorder(1)


# print(tree)
# print(parent)
