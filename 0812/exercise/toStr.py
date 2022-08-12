def myStr(i):


    s =''
    a = abs(i)

    while True:



        s = chr((a % 10) + ord('0')) + s
        a = a // 10
        if a == 0:
            if i < 0:
                s = '-' + s
                break
            break
    return s

print(myStr(123))
print(myStr(3214))
print(myStr(-321))

