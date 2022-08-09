# import sys
# sys.stdin = open('input.txt', 'r')

def getValueSum(N, M, num_lst):
    maxSum = 0
    minSum = 0
    for i in range(M):
        maxSum += num_lst[i]
        minSum += num_lst[i]

    for num in range(N - M + 1):
        mSum = 0
        for j in range(M):
            mSum += num_lst[num + j]
        if mSum > maxSum:
            maxSum = mSum
        elif mSum < minSum:
            minSum = mSum

    return maxSum, minSum




TC = int(input())


for tc in range(1, TC+1):

    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))


    a, b= getValueSum(N, M, num_lst)



    result = a - b



    print(f'#{tc} {result}')







