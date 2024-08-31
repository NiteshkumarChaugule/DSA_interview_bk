"""

data = [1, 3, 3, 3, 5, 7, 9]

:return
[[1, 1], [3, 3], [5, 1], [7, 1], [9, 1]]

"""


def count_n(data):
    resp = []
    count = 0
    for i in range(len(data)):
        if i+1 < len(data) and data[i] == data[i+1]:
            count += 1
        else:
            resp.append([data[i], count + 1])
            count = 0
    return resp


if __name__ == '__main__':
    print(f"Result: {count_n([1, 3, 3, 3, 5, 7, 9])}")


"""

def count_n(data):
    resp = []
    c = 1
    priv = -1
    for n in data:
        if n == priv:
            c += 1
        else:
            priv = n
            resp.append([n, c])
    return resp


"""