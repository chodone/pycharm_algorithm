
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

    newNum_lst = bubble_sort(num_lst, N)
    smallNum = []
    bigNum = []
    result = []

    if N % 2:
        smallNum = newNum_lst[:N//2]
        BigNum = newNum_lst[N//2:]
        result.append(BigNum[-1])
        for i in range(N//2):
            result.append(smallNum[i])
            result.append(BigNum[-i-2])

    else:
        smallNum = newNum_lst[:N // 2]
        BigNum = newNum_lst[N // 2:]

        for i in range(N//2):
            result.append(BigNum[-i - 1])
            result.append(smallNum[i])

    result = result[:10]

    print(f'#{tc}', *result)







