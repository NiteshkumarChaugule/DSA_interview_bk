"""
list1 = [(1,5),(2,4),(3,3),(2,2),(1,1)]

output:
[(1, 1), (2, 2), (3, 3), (2, 4), (1, 5)]

"""


def sort2(data):
    if len(data) == 0:
        return data
    p = data[-1]
    left = []
    right = []
    for d in data[:-1]:
        if p[1] > d[1]:
            left.append(d)
        else:
            right.append(d)
    return sort2(left) + [p] + sort2(right)


def sort_list(data):
    if len(data) <= 0:
        return []
    p = data[-1]
    left = []
    right = []

    for d in data[:-1]:
        if d[1] < p[1]:
            left.append(d)
        else:
            right.append(d)
    return sort_list(left)+[p]+sort_list(right)


print(f"sorted: {sort_list([(1, 5), (2, 4), (3, 3), (2, 2), (1, 1)])}")
print(f"sorted: {sort2([(1, 5), (2, 4), (3, 3), (2, 2), (1, 1)])}")
