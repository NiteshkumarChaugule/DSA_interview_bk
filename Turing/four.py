"""
most repeated character

Given:
1. "abcddefda1111133333333"
output: d

2. "AA0AB0BB0cc0aa0awo0BBBw123123"
output: "B"
"""


def most_repeated_char(string):
    max_char = ""
    max_count = 0
    visited = dict()
    for s in string:
        if not s.isalpha():
            continue
        if s not in visited:
            visited[s] = 1
        else:
            visited[s] += 1
        if visited[s] > max_count:
            max_char = s
            max_count = visited[s]
    return max_char


if __name__ == '__main__':
    inputs = ["abcddefda1111133333333", "AA0AB0BB0cc0aa0awo0BBBw123123"]
    for i in inputs:
        print(most_repeated_char(i))
