def mySum(lst):
    result = []
    for i in range(len(lst) - 1):
        result.append(lst[i] + lst[i+1])
    return result





def pascal(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        return [1, *mySum(pascal(n-1)), 1]


TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    print(f'#{tc}')
    for i in range(1, N+1):
        print(*pascal(i))


