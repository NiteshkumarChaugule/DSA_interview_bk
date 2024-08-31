"""
data = ["Steve jobs", "mark Zuckerberg", "bill gates", "Adele Goldberg"]

:output

['Steve Jobs', 'Mark Zuckerberg', 'Bill Gates', 'Adele Goldberg']
"""


def caps(data):
    resp = []
    for name in data:
        first, last = name.split()
        resp.append(f"{first.capitalize()} {last.capitalize()}")
    return resp


if __name__ == '__main__':
    _data = [
        "Steve jobs",
        "mark Zuckerberg",
        "bill gates",
        "Adele Goldberg"
    ]
    print(caps(_data))
