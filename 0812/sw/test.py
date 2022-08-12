TC = int(input())
for tc in range(1, TC+1):
    D, A, B = map(int, input().split())
    li = []

    for n in range(A,B+1):
        check = True
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                check = False
        if check:
            li.append(n)

    cnt = 0

    for i in li:
        for j in str(i):
            if int(j) == D:
                cnt += 1

    print(f'#{tc} {cnt}')