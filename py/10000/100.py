import sys
import time
import copy
import uuid

def process(lines, start_point):
    if not lines.get(start_point):
        return start_point, 0
    else:
        end_point = start_point
        max_length = 0;
        if not CACHE.get(start_point):
            for line in lines[start_point]:
                end_path, count = process(lines, line)
                if count + 1 > max_length or (count + 1 == max_length and int(end_path) < int(end_point)):
                    max_length = count + 1
                    end_point = end_path
            CACHE[start_point] = {
                'end_point': end_point,
                'max_length': max_length
            }
        else:
            end_point = CACHE[start_point]['end_point']
            max_length = CACHE[start_point]['max_length']
        return end_point, max_length

def main():
    start_time = time.time()
    data = sys.stdin.readlines()

    lines = {}
    case_count = 0
    while len(data) > 0:
        global CACHE
        CACHE = {}
        case_count += 1
        lines = {}
        number_of_line = data.pop(0).split()[0]
        if number_of_line == '0':
            break
        start_point = data.pop(0).split()[0]
        while True:
            start, end = data.pop(0).split()
            if start == '0' and end == '0':
                break
            # key = '{} {}'.format(start, end)
            if not lines.get(start):
                lines[start] = []
            lines[start].append(end)
        end_point, max_length = process(lines, start_point)
        print('Case {}: The longest path from {} has length {}, finishing at {}.\n'.format(case_count, start_point, max_length, end_point))
    # print(sys.stdin.readlines())
    # print("--- %s seconds ---" % (time.time() - start_time))

main()
