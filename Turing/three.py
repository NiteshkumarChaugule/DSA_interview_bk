"""
find longest substring

given:
1. "abcabcbb"
output: "abc", 3

2. "bbbbb"
output: "b", 1

3. "pwwkew"
output: "wke", 3

"""


def find_longest_substring(string):
    res = ""
    sub = ""
    for s in string:
        if s in sub:
            sub = sub[sub.index(s) + 1:] + s
        else:
            sub += s
        if len(sub) > len(res):
            res = sub
    return res, len(res)


if __name__ == '__main__':
    inputs = ["abcabcbb", "bbbb", "pwwkew", " @..", "", "a"]
    for i in inputs:
        print(find_longest_substring(i))
