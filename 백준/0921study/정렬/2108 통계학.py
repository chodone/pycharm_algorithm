# input() 보다 이게 더 빠르다고 하네..
import sys

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()

countDict = {}
for j in range(lst[0], lst[-1]+1):
    countDict[j] = 0

for k in lst:
    countDict[k] += 1



# 산술평균
avg = round(sum(lst) / len(lst))
print(avg)

# 중앙값
center = lst[N//2]
print(center)

# 최빈값
a = max(sorted(countDict.values()))
b = [k for k, v in countDict.items() if v == a]
b.sort()
print(b[1])


# 범위
c = lst[-1] - lst[0]
print(c)













