TC = int(input())

for tc in range(1, TC+1):
    A, B = input().split()
    cnt = 0
    minus_cnt = 0

    for idx in range(len(A)):
        if A[idx] == B[0]:
            for i in range(len(B)-1):
                if A[idx+i] != B[i]:
                    minus_cnt = 0

                    break
                minus_cnt += 1
                print(minus_cnt)
        cnt += 1

    result = cnt - minus_cnt
    print(f'#{tc} {result}')



