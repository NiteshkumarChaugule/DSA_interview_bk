"""
dct_list = ['abc', 'cab', 'abcd', 'dcba', 'abcde']

# {3: ['abc', 'cab'], 4: ['abcd', 'dcba'], 5: ['abcde']}

"""


def create_groups(data_list):
    resp = {}
    for d in data_list:
        n = len(d)
        if n in resp:
            resp[n].append(d)
        else:
            resp[n] = [d]
    return resp


if __name__ == '__main__':
    print(f"Grouped: {create_groups(['abc', 'cab', 'abcd', 'dcba', 'abcde'])}")
