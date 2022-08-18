

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())

    A_case = [0] * M

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    maxSum = 0

    if M > N:
        for i in range(M - N + 1):
            sum = 0
            for j in range(len(A)):
                sum += A[j] * B[j]
            B.pop(0)
            if maxSum < sum:
                maxSum = sum
    else:
        for i in range(N - M + 1):
            sum = 0
            for j in range(len(B)):
                sum += A[j] * B[j]
            A.pop(0)
            if maxSum < sum:
                maxSum = sum

    print(f'#{tc} {maxSum}')
