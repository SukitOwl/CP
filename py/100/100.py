import sys
import time


def two_n_plus_1(num, length=0, arr=None, cache=None):
    if arr is None:
        arr = []
    if cache is None:
        cache = {}
    if cache.get(num):
        length = length + cache.get(num)
        return length, arr

    arr.append(num)
    length = length + 1
    # print(int(num))
    if num == 1:
        # pass
        # print('Cycle length = {}'.format(length))
        return length, arr
    else:
        next_num = 0
        if num % 2 == 1:
            next_num = (3*num) + 1
        else:
            next_num = num / 2
        return two_n_plus_1(int(next_num), length=length, arr=arr, cache=cache)

def update_cache(cache, length, arr):
    for index, item in enumerate(arr):
        cache[int(item)] = length - index
    return cache

def step_back_range(start, end):
    while start >= end:
        yield start
        start -= 1

def main():
    start_time = time.time()
    cache = {}
    for line in sys.stdin:
        a, b = line.split()
        a = int(a)
        b = int(b)
        # a = int(sys.argv[1])
        # b = int(sys.argv[2])
        right = max(a, b)
        left = min(a, b)
        old_right = right
        old_max_length = 0
        # for n in step_back_range(right, left):
        while old_right >= left:
            n = old_right
            # print(n)
            value_on_cache = cache.get(n)
            if value_on_cache:
                if value_on_cache > old_max_length:
                    old_max_length = value_on_cache
                old_right = old_right - 1    
                continue
            length, arr = two_n_plus_1(n, cache=cache)
            cache = update_cache(cache, length, arr)
            if length > old_max_length:
                old_max_length = length
            old_right = old_right - 1
        print('{} {} {}'.format(a, b, old_max_length))
        # print('max_length = {}'.format(old_max_length))
        # print('cache state = {}'.format(cache))
    # print("--- %s seconds ---" % (time.time() - start_time))

main()
