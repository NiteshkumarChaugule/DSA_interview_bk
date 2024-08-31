"""

"aAcbBadEF" -> "cadEF"

"""


def rm_adj(string):
    resp = ""
    i = 0
    while i < len(string):
        if i + 1 < len(string) and string[i].lower() == string[i+1].lower():
            i += 2
        else:
            resp += string[i]
            i += 1
    return resp


if __name__ == '__main__':
    print(f'Result: {rm_adj("aAcbBadEF")}')


"""

def rm_adj2(string):
    resp = ""
    i = 0
    while i < len(string):
        if i + 1 == len(string):
            resp += string[i]
            break

        if string[i].islower():
            if i+1 > len(string):
                break
            if string[i].upper() == string[i+1]:
                i += 2
                continue
            else:
                resp += string[i]
                i += 1
        else:
            if i+1 > len(string):
                break
            if string[i].lower() == string[i+1]:
                i += 2
                continue
            else:
                resp += string[i]
                i += 1
    return resp

"""

