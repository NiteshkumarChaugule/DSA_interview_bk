"""
list1 = [(1,3),(2,2),(1,1)]
output:
[(1,1),(2,2),(1,3)]
"""


def sort_list(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            print(f"i={data[i][1]}; j={data[j][1]}")
            if data[i][1] > data[j][1]:
                data[i], data[j] = data[j], data[i]
                print(f"DATA: {data}")


def sort_list2(data):
    if len(data) == 0:
        return data
    p = data[-1]
    left = []
    right = []
    for d in range(len(data)-1):
        if data[d][1] < p[1]:
            left.append(data[d])
        else:
            right.append(data[d])
    return sort_list2(left) + [p] + sort_list2(right)


def in_place_sort(data, left, right):
    if left >= right:
        return

    def sort_sub(s, e):
        p = data[e]
        i = s - 1
        for j in range(s, e):
            if data[j][1] < p[1]:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i+1], data[e] = data[e], data[i+1]
        return i+1

    pivot = sort_sub(left, right)
    in_place_sort(data, left, pivot-1)
    in_place_sort(data, pivot+1, right)


list1 = [(1, 3), (2, 2), (1, 1)]
# sort_list(list1)
# print(f"sorted: {list1}")
# print(f"sorted: {sort_list2(list1)}")
new = list1.copy()
in_place_sort(new, 0, len(list1)-1)
print(f"sorted: {new}")
