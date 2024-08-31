"""
container with most water:

Given:
1. [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49

2, [1, 1]
Output: 1

"""


def max_size(heights):
    max_s = 0
    b1, b2 = 0, 0
    for i, p in enumerate(heights[:-1]):
        for j, q in enumerate(heights[i+1:]):
            new_s = (min(p, q)) * (j + 1)
            if max_s < new_s:
                max_s = new_s
                b1, b2 = p, q
    return max_s, b1, b2


if __name__ == '__main__':
    inputs = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1]]
    for ts in inputs:
        print(max_size(ts))
