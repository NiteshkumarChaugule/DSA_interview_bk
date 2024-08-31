"""
decorators...
"""

import time


def calc_time(func):
    def wrap(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f"Execution time {t2-t1} sec")
        return res
    return wrap


@calc_time
def my_func():
    time.sleep(1)
    print("execution in my function")


print(my_func())


