import sys # sys 모듈을 import
input = sys.stdin.readline

def bubble_sort(lst, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if lst[j][0] > lst[j+1][0]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            elif lst[j][0] == lst[j+1][0]:
                if lst[j][1] > lst[j+1][1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# bubllesort 막혔다~~
# input 받으면서 정렬은 불가능할까 ??





TC = int(input())

lst = []
for i in range(TC):
    X, Y = map(int, input().split())
    lst.append((X, Y))


bubble_sort(lst, len(lst))

for j in lst:
    print(*j)
