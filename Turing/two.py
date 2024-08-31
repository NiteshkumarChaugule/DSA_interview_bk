

def cal_points(ops):
    result = []
    for s in ops:
        try:
            result.append(int(s))
        except ValueError:
            if "+" == s:
                result.append(result[-1]+result[-2])
            elif "C" == s:
                result.pop()
            else:
                result.append(result[-1]*2)
    return sum(result)


if __name__ == '__main__':
    # line = input().strip().split()
    line = ["5", "2", "C", "D", "+"]
    dd = cal_points(line)
    print(f"{dd}")
