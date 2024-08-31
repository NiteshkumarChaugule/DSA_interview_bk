"""
Given two given lists [1,3,6,78,35,55] and [12,24,35,55,88,78,155],
write a program to make a list whose elements are intersection of the above given lists.
"""


def get_intersection(list1, list2):
    return list(set(list1).intersection(set(list2)))


if __name__ == '__main__':
    print(f'Result: {get_intersection([1,3,6,78,35,55], [12,24,35,55,88,78,155])}')
