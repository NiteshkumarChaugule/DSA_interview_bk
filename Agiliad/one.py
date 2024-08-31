"""
s1 = "my name is aditya"

output:
********
*my    *
*name  *
*is    *
*aditya*
********

"""


def formatted_print(string):
    data = string.split()
    max_length = 0
    for d in data:
        if len(d) > max_length:
            max_length = len(d)
    print("*" * (max_length+2))
    for d in data:
        print("*{}{}*".format(d, " " * (max_length - len(d))))
    print("*" * (max_length+2))


if __name__ == '__main__':
    formatted_print("my name is aditya")
