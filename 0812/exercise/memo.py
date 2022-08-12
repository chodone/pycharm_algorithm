# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] + 'c'
#
# print(s1 == s2, s1 is s2)
# print(id(s1), id(s2))
# print(s1 == s3, s1 is s3)
# print(s1 == s4, s1 is s4)
# print(s1 == s2, s1 is s5)


def myStrcmp(a, b):

    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1


print(myStrcmp('abcd', 'b'))
print(myStrcmp('b', 'abcd'))
print(myStrcmp('abcd', 'abcd'))




