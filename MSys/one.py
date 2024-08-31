"""
1.
Input : ABBCCCDDDDE

Output : A1B2C3D4E1

2.
Input : ABBCCCDDDDEA

Output : A1B2C3D4E1A1

"""
s = 2


def solution(txt):
    res = []
    for c in txt:
        if len(res) > 1 and res[-2] == c:
            res[-1] = str(int(res[-1]) + 1)
        else:
            res.extend([c, "1"])
    return "".join(res)


if __name__ == "__main__":
    print(solution("ABBCCCDDDDE"))
