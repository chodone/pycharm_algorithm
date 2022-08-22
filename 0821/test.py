def countingSort(data):

    counts = [0] * 20
    result = [0] * len(data)


    for i in range(0, len(data)):
        counts[data[i]] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    print(counts)

    for i in range(len(data)-1, -1, -1):
        counts[data[i]] -= 1
        result[counts[data[i]]] = data[i]

    return result


