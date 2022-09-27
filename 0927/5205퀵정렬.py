def partitionH(L, R):
    p = L
    i = L + 1
    j = R

    while i <= j:
        while i <= j and lst[i] <= lst[p]:
            i += 1

        while i <= j and lst[j] > lst[p]:
            j -= 1

        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    lst[p], lst[j] = lst[j], lst[p]

    return j


def quick_s(L, R):
    if L < R:
        p = partitionH(L, R)
        quick_s(L, p-1)
        quick_s(p+1, R)


TC = int(input())

for tc in range(1 , TC +1):
    N = int(input())
    lst = list(map(int, input().split()))

    quick_s(0, len(lst)-1)



    print(f'#{tc} {lst[N//2]}')