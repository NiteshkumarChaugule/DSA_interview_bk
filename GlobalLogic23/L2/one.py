"""


dict1 = {'a':[10],'b':[10,20,30],'c':[10,20],'d':[10,20,30,40]}

output- [{'d': [10, 20, 30, 40]}, {'b': [10, 20, 30]}, {'c': [10, 20]}, {'a': [10]}]

"""


def sort_dict(data_dict):
    def sort_list(data_list):
        if len(data_list) <= 1:
            return data_list
        p = data_list.pop()
        list1 = []
        list2 = []
        for d in data_list:
            if len(data_dict[d]) < len(data_dict[p]):
                list1.append(d)
            else:
                list2.append(d)
        return sort_list(list1) + [p] + sort_list(list2)
    resp = sort_list(list(data_dict.keys()))
    return [{k: data_dict[k]} for k in resp[::-1]]


if __name__ == '__main__':
    r = {'a': [10], 'b': [10, 20, 30], 'c': [10, 20], 'd': [10, 20, 30, 40]}

    print(f"sorted: {sort_dict(r)}")
