"""

output:
1 2 3 5 8 13 21 34 55 89
"""

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    for i in range(1, 11):
        print(fib(i), end=" ")

