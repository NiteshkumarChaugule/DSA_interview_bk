"""
[121, 23, "abc", "abcba"]
"""


def is_palindrome(item):
    if not isinstance(item, str):
        item = str(item)
    return "".join(list(item)[::-1]) == item


def filter_palindrome(data):
    return [d for d in data if is_palindrome(d)]


if __name__ == '__main__':
    _d = [121, 23, "abc", "abcba"]
    print(f"{filter_palindrome(_d)}")
