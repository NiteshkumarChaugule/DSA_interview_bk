"""
n=3

output:
['((()))', '(()())', '(())()', '()(())', '()()()']
"""


def generate_p(n):
    ans = []

    def _generate(_op, _cl, s):
        if _op == _cl == n:
            ans.append(s)
        if _op < n:
            _generate(_op + 1, _cl, s+"(")
        if _cl < _op:
            _generate(_op, _cl + 1, s+")")

    _generate(0, 0, "")
    return ans


print(generate_p(3))
