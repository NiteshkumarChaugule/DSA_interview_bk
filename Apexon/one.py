"""
generator

decorator
"""
import time
from random import choice


def time_it(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        resp = func(*args, **kwargs)
        print(f"Execution time: {time.time() - t1}")
        return resp
    return wrapper


@time_it
def my_generator(a1, a2=10):
    print(f"my_generator: A1={a1}; A2={a2}")
    choice_from = list(range(a1, a2+1))
    while 1:
        if len(choice_from) == 0:
            break
        g = choice(choice_from)
        choice_from.remove(g)
        time.sleep(2)
        yield g


if __name__ == '__main__':
    g = my_generator(2, a2=5)
    for j in range(4):
        print(g.__next__())
