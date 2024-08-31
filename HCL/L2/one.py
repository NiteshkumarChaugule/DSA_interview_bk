"""
*****
 ****
  ***
   **
    *
"""


def print_stars(n):
    init_n = n
    while n >= 0:
        print("{}{}".format(" " * (init_n-n), "*" * n))
        n -= 1


if __name__ == '__main__':
    print_stars(5)
