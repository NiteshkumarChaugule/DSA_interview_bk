"""
List a contains 100 words, many of them are duplicate,
write a two line code which removes duplicates preserving the order of list.
"""


def get_unique_and_ordered(words):
    return sorted(set(words), key=words.index)


if __name__ == '__main__':
    wds = ["one", "two", "three", "one", "four", "three", "one", "four", "five"]
    print(f"{get_unique_and_ordered([1, 1, 9, 1, 9, 6, 9, 7])}")
    print(f"{get_unique_and_ordered(wds)}")
