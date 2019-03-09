import sys
import time

block_cache = []
position_cache = {}

def move_onto(start, end):
    onto(end)
    move_over(start, end)

def move_over(start, end):
    destination = position_cache[end]['position']
    if position_cache[start]['early'] is not None:
        position_cache[position_cache[start]['early']]['after'] = None
    if len(block_cache[destination]) != 0:
        top_of_destination = block_cache[destination][len(block_cache[destination]) - 1]
        position_cache[top_of_destination]['after'] = start
        position_cache[start]['early'] = top_of_destination
    if position_cache[start]['after'] is not None:
        over(position_cache[start]['after'])
    block_cache[position_cache[start]['position']].pop(len(block_cache[position_cache[start]['position']]) - 1)
    block_cache[destination].append(start)
    position_cache[start]['position'] = destination

def pile_onto(start, end):
    onto(end)
    pile_over(start, end)

def pile_over(start, end):
    origin = position_cache[start]['position']
    destination = position_cache[end]['position']
    if position_cache[start]['early'] is not None:
        position_cache[position_cache[start]['early']]['after'] = None
    if len(block_cache[destination]) != 0:
        top_of_destination = block_cache[destination][len(block_cache[destination]) - 1]
        position_cache[top_of_destination]['after'] = start
        position_cache[start]['early'] = top_of_destination
    arr = pile(start, origin, destination)
    block_cache[destination].extend(arr)

def pile(start, origin, destination, arr=None):
    if arr is None:
        arr = [start]
    else:
        arr.append(start)
    position_cache[start]['position'] = destination
    block_cache[origin].pop(len(block_cache[origin]) - 1)
    if position_cache[start]['after'] is not None:
        pile(position_cache[start]['after'], origin, destination, arr=arr)
    return arr

def onto(end):
    if position_cache[end]['after'] is not None:
        over(position_cache[end]['after'])

def over(start_after):
    if position_cache[start_after]['after'] is not None:
        over(position_cache[start_after]['after'])
    block_cache[position_cache[start_after]['position']].pop(len(block_cache[position_cache[start_after]['position']]) - 1)
    block_cache[start_after].append(start_after)
    position_cache[position_cache[start_after]['early']]['after'] = None
    position_cache[start_after]['early'] = None
    position_cache[start_after]['position'] = start_after

def main():
    # try:
    # ==========

    start_time = time.time()
    for line in sys.stdin:
        b = line.split()
        if len(b) == 1:
            if b[0] == 'quit':
                pass
            else:
                for x in range(0, int(b[0])):
                    block_cache.append([x])
                    position_cache[x] = {
                        'early': None,
                        'position': x,
                        'after': None
                    }
        else:
            start = int(b[1])
            end = int(b[3])
            if start == end:
                continue
            elif position_cache[start]['position'] == position_cache[end]['position']:
                continue
            else:
                start = int(b[1])
                end = int(b[3])
                command = '{}_{}'.format(b[0], b[2])
                if command == 'move_onto':
                    move_onto(start, end)
                elif command == 'move_over':
                    move_over(start, end)
                elif command == 'pile_onto':
                    pile_onto(start, end)
                else:
                    pile_over(start, end)

    for idx, x in enumerate(block_cache):
        space = '' if len(x) == 0 else ' '
        print('{}:{}{}'.format(idx, space, (' ').join(str(y) for y in x)))
    # print(position_cache)
    # print("--- %s seconds ---" % (time.time() - start_time))

    # ==========
    # except Exception:
    #     print(block_cache)
    #     print(position_cache)
    #     for key, value in position_cache.items():
    #         print(key)
main()
