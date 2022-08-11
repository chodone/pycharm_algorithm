
def mySum(lst):

    result = 0

    for i in lst:
        result += i

    return result



TC = int(input())

for tc in range(1, TC+1):
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    n = len(arr)
    cnt = 0


    N, K = map(int, input().split())

    for i in range(1<<n):
        result = []
        for j in range(n):
            if i & (1<<j):
                result.append(arr[j])

        if len(result) == N and mySum(result) == K:
            cnt += 1

    print(f'#{tc} {cnt}')







