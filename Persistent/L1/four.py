

class A(object):
    x = 1


class B(A):
    pass


class C(A):
    pass


print(A.x, B.x, C.x)
B.x = 2
print(A.x, B.x, C.x)
A.x = 3
print(A.x, B.x, C.x)
a = A()
a.x = 5
print(A.x, a.x, B.x, C.x)


# lst = [1, 2, 3, 4, 5]
#
# print(lst[10:])
#
# t = ("1", 2, ["three"])
#
# t[2].append("four")
#
# print(t)
