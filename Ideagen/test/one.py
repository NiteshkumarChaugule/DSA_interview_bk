"""
Write a program which takes following two lists as input

A = [“Ali”,”Hamza”,”Usman”]
B = [ [ 23, 29, 32], [ 5.8, 5.9, 6.1] ...]

and gives following output:

Ali is 23 years old and his height is 5.8ft
Hamza is 29 years old and his height is 5.9ft.
"""


def print_details(names, info):
    for name, details in zip(names, zip(*info)):
        print(f"{name} is {details[0]} years old and his height is {details[1]}ft")


if __name__ == '__main__':
    A = ["Ali", "Hamza", "Usman"]
    B = [[23, 29, 32], [5.8, 5.9, 6.1]]
    print_details(A, B)
