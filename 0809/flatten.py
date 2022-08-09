def countingSort(data):
    counts = [0] * 100

    for i in range(0, len(data)):
        counts[data[i] - 1] += 1

    return counts


TC = 10

for tc in range(1, TC + 1):
    N = int(input())

    height_lst = list(map(int, input().split()))

    count_lst = countingSort(height_lst)
    print(count_lst)

    for dump in range(N):
        for j in range(len(count_lst) - 1, -1, -1):

            if not count_lst[j]:
                continue
            else:
                count_lst[j] -= 1
                count_lst[j - 1] += 1
                break

        for m in range(len(count_lst)):
            if not count_lst[m]:
                continue
            else:
                count_lst[m] -= 1
                count_lst[m + 1] += 1
                break

    if count_lst[m] == 0:
        m += 1
    if count_lst[j] == 0:
        j -= 1
    print(count_lst, j, m)
    # print(f'#{tc} {j-m}')