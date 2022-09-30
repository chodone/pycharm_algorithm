def merge(lLst, rLst):
    global cnt
    lp = rp = 0
    result = []
    while lp < len(lLst) and rp < len(rLst):
        if lLst[lp] < rLst[rp]:
            result.append(lLst[lp])
            lp += 1
        else:
            result.append(rLst[rp])
            rp += 1
    if lLst[-1] > rLst[-1]:
        cnt += 1

    result.extend(lLst[lp:])
    result.extend(rLst[rp:])
    return result

# lst의 정보를 정렬하여 새로운 리스트를 return
def merge_s(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = merge_s(lst[:mid])
    right = merge_s(lst[mid:])
    result = merge(left, right)
    return result





TC = int(input())
for tc in range(1, TC +1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    res = merge_s(arr)
    print(f'#{tc} {res[N//2]} {cnt}')