"""
print stars:

    *
   ***
  *****
 *******
*********
"""


def print_stars(n):
    for i in range(1, n + 1, 2):
        print("{}{}".format(" " * ((n - i) // 2), "*" * i))


if __name__ == '__main__':
    print_stars(9)
