def binarySearch(l, r, key):
    global cnt
    m = (l+r) // 2
    flag = 0
    while A[m] != key:

        if flag == 0:
            if key > A[m]:
                l = m + 1
                m = ((m+1) + r) // 2
                flag = 2  # flag = 2 는 A[m]보다 큰 오른쪽
            else:
                r = m - 1
                m = (l + (m-1)) // 2
                flag = 1 # flag = 1 은 A[m]보다 작은 왼쪽

        elif flag == 1:
            if key < A[m]:
                return
            l = m + 1
            m = ((m+1) + r) // 2
            flag = 2


        elif flag == 2:
            if key > A[m]:
                return
            r = m - 1
            m = (l + (m - 1)) // 2
            flag = 1


    #while문 탈출
    cnt += 1






TC = int(input())

for tc in range(1, TC + 1):
    N, M = map(int, input().split())

    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0

    for b in B:
        if b in A:
            binarySearch(0, N-1, b)



    print(f'#{tc} {cnt}')
