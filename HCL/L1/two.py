"""
algorithm for quick sort
"""


def quick_sort(data):
    if len(data) <= 1:
        return data
    p = data.pop()
    left = []
    right = []
    for d in data:
        if d < p:
            left.append(d)
        else:
            right.append(d)
    return quick_sort(left) + [p] + quick_sort(right)


if __name__ == '__main__':
    print(f"{quick_sort([5, 4, 6, 7, 2, 3, 1, 1])}")
