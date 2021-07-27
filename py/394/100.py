import sys
import time


def main():
    start_time = time.time()
    head = None
    arr = {}
    # {
    #     "key": {
    #         "base": 0,
    #         "sizeof": 0,
    #         "dimensions": 1,
    #         "bound": [
    #             { "min": 0, "mix": 0, "size": 0
    #             }
    #         ]
    #     }
    # }
    for line in sys.stdin:
        information = line.split()
        if head is None:
            head = [int(information[0]), int(information[1])]
        elif not information[0] in arr:
            arr[information[0]] = {
                "base": int(information[1]),
                "sizeof": int(information[2]),
                "dimensions": int(information[3]),
                "bound": [None] * int(information[3]),
            }
            for i in range(int(information[3])):
                arr[information[0]]["bound"][int(information[3]) - 1 - i] = {
                    "min": int(
                        information[4 + (2 * (int(information[3]) - 1)) - 2 * i]
                    ),
                    "max": int(
                        information[5 + (2 * (int(information[3]) - 1)) - 2 * i]
                    ),
                    "size": int(information[2])
                }
                if i != 0:
                    arr[information[0]]["bound"][int(information[3]) - 1 - i][
                        "size"
                    ] = arr[information[0]]["bound"][int(information[3]) - 1 - i + 1][
                        "size"
                    ] * (
                        1
                        + arr[information[0]]["bound"][int(information[3]) - 1 - i + 1][
                            "max"
                        ]
                        - arr[information[0]]["bound"][int(information[3]) - 1 - i + 1][
                            "min"
                        ]
                    )
        else:
            shift = arr[information[0]]["base"]
            for i in range(1, len(information)):
                shift = shift + (int(information[i]) - arr[information[0]]["bound"][i - 1]["min"]) * arr[information[0]]["bound"][i - 1]["size"]
            int_arr = []
            for i in information[1:]:
                int_arr.append(int(i))
            print(f"{information[0]}{int_arr} = {shift}")
    # print("--- %s seconds ---" % (time.time() - start_time))


main()
