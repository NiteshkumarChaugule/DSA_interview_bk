"""
Decorators

"""


def correct(f):
    def wrapper(n1, n2):
        if n1 < n2 or n2 == 0:
            n1, n2 = n2, n1
        return f(n1, n2)
    return wrapper


@correct
def divide(n1, n2):
    return n1//n2


if __name__ == '__main__':
    print(divide(2, 0))
