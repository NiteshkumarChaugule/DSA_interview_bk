
def quick_sort(data):
    if len(data) <= 1:
        return data
    p = data[-1]
    left = []
    right = []
    for d in data[:-1]:
        if d < p:
            left.append(d)
        else:
            right.append(d)
    return quick_sort(left) + [p] + quick_sort(right)


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


if __name__ == '__main__':
    my_list = [5, 4, 6, 7, 2, 3, 1, 1]
    print(f"Sorted list: {quick_sort(my_list)}")
    print(f"List after 1st sort: {my_list}")
    # in_place_sort(my_list, 0, len(my_list) - 1)
    # print(f"List after 2nd sort: {my_list}")
