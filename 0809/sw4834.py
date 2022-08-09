import sys
sys.stdin = open("input.txt", "r")


def countingSort(data):

    counts = [0] * 10
    result = [0] * len(data)


    for i in range(0, len(data)):
        counts[data[i]] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    for i in range(len(data)-1, -1, -1):
        counts[data[i]] -= 1
        result[counts[[data[i]]]] = data[i]

    return result




def maxCount(data):
    counts = [0] * 10


    for i in range(0, len(data)):

        counts[int(data[i])] += 1

    return counts








TC = int(input())


for tc in range(1, TC + 1):

    N = int(input())
    card_lst = list(input())
    V = maxCount(card_lst)

    maxCnt = 0
    maxNum = 0
    i = 0

    for cnt in V:

        if cnt >= maxCnt:
            maxCnt = cnt
            maxNum = i
        i += 1


    print(f'#{tc} {maxNum} {maxCnt}')








