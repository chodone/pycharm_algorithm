import sys
sys.stdin = open("input.txt", "r")


def bubble_sort(lst, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst







TC = int(input())


for tc in range(1, TC+1):
    N = int(input())
    num_lst = list(map(int, input().split()))

    a = bubble_sort(num_lst, len(num_lst))

    result = a[-1] - a[0]

    print(f'#{tc} {result}')

