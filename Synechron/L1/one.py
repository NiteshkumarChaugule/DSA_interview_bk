"""
{[]{()}}

output:
balanced/unbalanced

"""


def check(data):
    mapping = {"{": ["curly", 1], "(": ["round", 1], "[": ["square", 1], "}": ["curly", -1], ")": ["round", -1],
               "]": ["square", -1]}
    brackets = {"curly": 0, "round": 0, "square": 0}
    for d in data:
        name, val = mapping[d]
        brackets[name] += val
        if brackets[name] < 0:
            return "unbalanced"
    return "balanced"


if __name__ == '__main__':
    print(f'Result: {check("}{}{{[]{()}}")}')
    print(f'Result: {check("{[]{()}}")}')
