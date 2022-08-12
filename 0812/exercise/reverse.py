
def myReverse(s):
    s = list(s)
    n = len(s)


    for idx in range(n//2):
        mid = []

        mid = s[n-idx-1]
        s[n-idx-1] = s[idx]
        s[idx] = mid

    a = ''.join(s)


    print(a)









s = 'Reverse this strings'
myReverse(s)

