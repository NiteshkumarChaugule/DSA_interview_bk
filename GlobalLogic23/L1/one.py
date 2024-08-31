"""
dct_list = ['abc', 'cab', 'abcd', 'dcba', 'abcde']
 # {3: ['abc', 'cab'], 4: ['abcd', 'dcba'], 5: ['abcde']}

"""


def create_groups(data):
    resp = {}
    for d in data:
        length = len(d)
        if length in resp:
            resp[length].append(d)
        else:
            resp[length] = [d]
    return resp


if __name__ == '__main__':
    print(f"Grouped: {create_groups(['abc', 'cab', 'abcd', 'dcba', 'abcde'])}")
