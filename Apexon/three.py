"""
count letters
"""

def count(string):
    res = dict()
    for s in string:
        if s in res:
            res[s] += 1
        else:
            res[s] = 1
    return res


if __name__ == '__main__':
    name = "niiiteeeeshh"
    print(count(name))
