from pprint import pprint
Arr = [[0] * 100 for _ in range(100)]
for i in range(4):
    lst = list(map(int, input().split()))

    for row in range(lst[0], lst[2]):
        for col in range(lst[1], lst[3]):
            Arr[row][col] = 1


cnt = 0
for line in Arr:
    for i in line:
        if i == 1:
            cnt += 1
print(cnt)