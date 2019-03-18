import sys
import time

flag = {
    "open": True
}

def check(c):
    if c != '"':
        return c
    if flag['open']:
        flag['open'] = False
        return '``'
    else:
        flag['open'] = True
        return "''"


def main():
    start_time = time.time()
    for line in sys.stdin:
        new_line = ''
        for c in line:
            if c != '\n':
                new_line = new_line + check(c)
        print(new_line)

    # print("--- %s seconds ---" % (time.time() - start_time))

main()
