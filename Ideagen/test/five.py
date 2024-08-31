"""
Write a recursive function which calculates 1+2+3+...+10

e.g. sum_recursive (start = 1 , end = 10)
   output = 55

sum_recursive (start = 5 , end = 10)
   output = 45

"""


def sum_recursive(start, end):
    if end == start:
        return end
    return end + sum_recursive(start, end-1)


if __name__ == '__main__':
    print(sum_recursive(1, 10))
