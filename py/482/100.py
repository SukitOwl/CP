import sys
import time


def main():
    start_time = time.time()
    head = None
    buffer = []
    is_order = True
    is_skip = False
    is_first = True
    for line in sys.stdin:
        information = line.split()
        if head is None:
            head = int(information[0])
            is_skip = True
            continue
        if is_skip:
            is_skip = False
            continue
        if is_order:
            is_order = False
            buffer = information
        else:
            if is_first:
                is_first = False
            else:
                print("")
            result = [None] * len(information)
            for i in range(len(information)):
                result[int(buffer[i]) - 1] = information[i]
            for i in result:
                print(i)
            is_order = True
            is_skip = True

    # print("--- %s seconds ---" % (time.time() - start_time))


main()
