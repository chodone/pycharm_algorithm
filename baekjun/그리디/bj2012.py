# from collections import deque
#
# def ranking(k, curV):
#     global minV
#
#     if k == 5:
#         minV = min(minV, curV)
#         return
#
#     elif curV >= minV:
#         return
#
#     for i in range(1, N+1):
#         if not Used[i]:
#             Used[i] = True
#             realRank.append(predRank[i])
#             ranking(k+1,  curV + abs(len(realRank) - 1 - predRank[i]))
#             Used[i] = False
#             realRank.pop()
#
#
# N = int(input())
# predRank = [0]
# for _ in range(N):
#     predRank.append(int(input()))
# realRank = [0]
# Used = [False] * (N+1)
# Used[0] = True
# minV = 1e10
#
# for i in range(1, N+1):
#     Used[i] = True
#     realRank.append(predRank[i])
#     ranking(1, abs(len(realRank) - 1 - predRank[i]))
#     Used[i] = False
#     realRank.pop()
#
# print(minV)

n = int(input())
expectedRank = []
for _ in range(n):
    expectedRank.append(int(input()))

expectedRank.sort()

result = 0
for i in range(1, n+1):
    result += abs(i-expectedRank[i-1])
print(result)


