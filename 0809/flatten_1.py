def bubble_sort(lst, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

TC = 10

for tc in range(1, TC+1):
    cnt = 0
    N = int(input())
    num_lst = list(map(int, input().split()))

    while cnt < N:
        num_lst = bubble_sort(num_lst, len(num_lst))
        num_lst[-1] -= 1
        num_lst[0] += 1
        cnt += 1

    num_lst = bubble_sort(num_lst, len(num_lst))
    result = num_lst[-1] - num_lst[0]

    print(f'#{tc} {result}')
