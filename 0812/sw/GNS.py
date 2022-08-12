import sys
sys.stdin = open("input.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    N = int(input()[3:])

    number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    count = [0] * 10


    num_lst = list(input().split())
    result = [0] * len(num_lst)

    for num1 in num_lst:
        for idx in range(len(number)):
            if num1 == number[idx]:
                count[idx] += 1


    for i in range(len(count)-1):
        count[i+1] += count[i]

    for i in range(len(num_lst)-1, -1, -1,):
        for idx in range(len(number)):
            if number[idx] == num_lst[i]:
                count[idx] -= 1
                result[count[idx]] = number[idx]



    print(f'#{tc}')
    print(*result)


