def rec(k, flag, sr, sc):
    if k == 1:

        cnt[Arr[sr][sc]] += 1
        return

    for row in range(k):
        for col in range(k):
            if Arr[sr + row][sc + col] == flag:continue
            for i in range(0, k, k//2):
                for j in range(0, k, k//2):
                    rec(k//2, Arr[sr+i][sc+j], sr + i, sc + j)
            return

    cnt[flag] += 1



N = int(input())

Arr = [list(map(int, input().split()))for _ in range(N)]
cnt = [0, 0]

rec(N, Arr[0][0], 0, 0)
print(cnt[0])
print(cnt[1])
