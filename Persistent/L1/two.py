"""
Given the value of n, i.e, number of lines, print the Fibonacci Triangle
E.g.
Input : n = 5
Output :
1
1 2
3 5 8
13 21 34 55
89 144 233 377 610

Input : n = 3
Output :
1
1 2
3 5 8
"""


def fib(n):
    a = 0
    b = 1
    for i in range(1, n+1):
        if i == 1:
            print(b)
            continue
        for j in range(i):
            print(a+b, end=" ")
            a, b = b, a + b
        print("")


if __name__ == '__main__':
    fib(5)
    fib(3)
