"""
find minimum number in unsorted list
"""

def get_min(my_list):
    m = my_list[0]
    for n in my_list[1:]:
        if n < m:
            m = n
    return m


if __name__ == '__main__':
    l1 = [5, 4, 3, 2, 1]
    print(get_min(l1))

