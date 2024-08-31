"""
[14:23] Ashish Singh

l1 = [1,3,5,6,10]
l2 = [2,4,5,5,6,8,9]

output:
[1, 2, 3, 4, 5, 5, 5, 6, 6, 8, 9, 10]

"""
import time


def timeit(f):
    def wrap(*args, **kwargs):
        t1 = time.time()
        r = f(*args, **kwargs)
        t2 = time.time()
        print(f"Finished in {t2 - t1} sec")
        return r
    return wrap


@timeit
def combine(data1, data2):
    time.sleep(1)
    p1 = 0
    p2 = 0
    result = []
    while True:
        if p1 >= len(data1):
            result.extend(data2[p2:])
            break
        if p2 >= len(data2):
            result.extend(data1[p1:])
            break
        d1 = data1[p1]
        d2 = data2[p2]
        if d1 < d2:
            result.append(d1)
            p1 += 1
        else:
            result.append(d2)
            p2 += 1
    return result


if __name__ == '__main__':
    l1 = [1, 3, 5, 6, 10]
    l2 = [2, 4, 5, 5, 6, 8, 9]
    print(combine(l1, l2))
