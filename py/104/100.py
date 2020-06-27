import sys
import time


def compare(a, b):
    a_lt_b = 0
    a_gt_b = 0
    for i in range(len(a)):
        if a[i] < b[i]:
            a_lt_b += 1
        elif a[i] > b[i]:
            a_gt_b += 1

    if a_lt_b == len(a):
        return -1
    elif a_gt_b == len(a):
        return 1
    else:
        return 0


def lcompare(n, sorted_box, graph):
    for i in range((len(sorted_box) - 1) - n):
        graph[n][i+1+n] = compare(sorted_box[n]["x"], sorted_box[i+1+n]["x"])
    return graph


def order(boxs):
    b = [{"n": i["n"], "x": '-'.join(["%07d" % j for j in i["x"]])} for i in boxs]
    b.sort(key = lambda i: i["x"])
    sorted_box = [{"n": i["n"], "x": [int(j) for j in i["x"].split("-")]} for i in b]

    graph = []
    for i in range(len(sorted_box)):
        graph.append([None] * len(sorted_box))
        graph = lcompare(i, sorted_box, graph)

    cache = {}

    longest_path = {
        "length": 1,
        "path": [len(sorted_box) - 1]
    }

    for i in range(len(sorted_box)):
        index = len(sorted_box) - 1 - i
        cache[index] = {
            "length": 1,
            "path": [index]
        }

        this_index_longest = 1
        this_index_path = [index]

        for j in range(len(sorted_box) - 1 - index):
            index2 = len(sorted_box) - 1 - j
            if graph[index][index2] == -1:
                if cache[index]["length"] + cache[index2]["length"] > this_index_longest:
                    this_index_longest = cache[index]["length"] + cache[index2]["length"]
                    this_index_path = cache[index]["path"] + cache[index2]["path"]
        cache[index]["length"] = this_index_longest
        cache[index]["path"] = this_index_path

        if cache[index]["length"] > longest_path["length"]:
            longest_path["length"] = cache[index]["length"]
            longest_path["path"] = cache[index]["path"]

    print(longest_path["length"])
    path = []
    for i in longest_path["path"]:
        # print(sorted_box[i]["x"])
        path.append(str(sorted_box[i]["n"]))
    print(' '.join(path))

    # print(boxs)
    # print(sorted_box)


def main():
    # start_time = time.time()
    head_line = True
    for line in sys.stdin:
        # print(line)
        if head_line:
            boxs = []

            a, b = line.split()
            a = int(a)
            b = int(b)

            number_of_box = a
            number_of_dimentsion = b

            box_at = 0
            head_line = False
            continue
        else:
            boxs.append({})
            boxs[box_at]['n'] = box_at + 1
            boxs[box_at]['x'] = [int(x) for x in line.split()]
            boxs[box_at]['x'].sort()
            box_at += 1
            if box_at == number_of_box:
                order(boxs)
                head_line = True

    # print("--- %s seconds ---" % (time.time() - start_time))

main()
