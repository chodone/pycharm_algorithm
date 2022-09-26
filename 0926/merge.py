def merge(lLst, rLst):
    lp = rp = 0
    result = []
    while lp < len(lLst) and rp < len(rLst):
        if lLst[lp] < rLst[rp]:
            result.append(lLst[lp])
            lp += 1
        else:
            result.append(rLst[rp])
            rp += 1
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

arr = [69, 10, 30, 2, 16, 8, 31, 22]
print(merge_s(arr))

