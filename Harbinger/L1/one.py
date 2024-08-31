"""
["india", "russia", "america", "south africa", "china"]

:output

["china", "india", "russia", "america", "south africa"]

"""


def sort_data(data):
    if len(data) <= 1:
        return data
    list1 = []
    list2 = []
    p = data[-1]
    for i in range(len(data)-1):
        if len(data[i]) < len(p):
            list1.append(data[i])
        else:
            list2.append(data[i])
    return list1 + [p] + list2


if __name__ == '__main__':
    _data = ["india", "russia", "america", "south africa", "china"]
    print(f"sorted: {sort_data(_data)}")

