"""
print prime numbers till 100

2, 3, 5, 7, 11, 13, 17...

"""


def print_prime(n):
    for i in range(2, n + 1):
        for j in range(2, i//2+1):
            if i % j == 0:
                break
        else:
            print(i)


if __name__ == '__main__':
    print_prime(100)