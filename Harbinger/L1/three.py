"""
find max occurred character

a = ['a', 's', 'r', 'a', 't', 'w', 't', 'a', 'b', 'a', 'b', 's', 'c']

output: a

"""


def find(data):
    count_map = {}
    max_occ = 0
    ch = ""
    for d in data:
        count_map[d] = count_map.get(d, 0) + 1
        if count_map[d] > max_occ:
            max_occ = count_map[d]
            ch = d
    return ch


if __name__ == "__main__":
    print(f"{find(['a', 's', 'r', 'a', 't', 'w', 't', 'a', 'b', 'a', 'b', 's', 'c'])}")
