import sys
import time

color_map = {
    0: 'B',
    1: 'G',
    2: 'C'
}

def process(data, colors, cache, num=0):
    if len(colors) == 1:
        result = cal(data, colors, cache, num)
        return [
            {
                'value': result,
                'route': colors
            }
        ]

    result = []
    for inx, color in enumerate(colors):
        next_colors = list(filter(lambda x: x != color, colors))
        next_num = num+1
        sum_of_child = process(data, next_colors, cache, num=next_num)
        sum_of_current_color = cal(data, [color], cache, num)
        for idx, x in enumerate(sum_of_child):
            x['route'].append(color)
            x['value'] = x['value'] + sum_of_current_color

            if num == 0 and len(result) != 0:
                if x['value'] < result[0]['value']:
                    result[0]['value'] = x['value']
                    result[0]['route'] = x['route']
                elif x['value'] == result[0]['value'] and alpha(x['route'], result[0]['route']):
                    result[0]['value'] = x['value']
                    result[0]['route'] = x['route']
            else:
                result.append(
                    {
                        'value': x['value'],
                        'route': x['route']
                    }
                )

            # result.append(
            #     {
            #         'value': x['value'],
            #         'route': x['route']
            #     }
            # )

    return result

def alpha(new, old):
    old_str = '{}{}{}'.format(color_map[old[2]], color_map[old[1]], color_map[old[0]])
    new_str = '{}{}{}'.format(color_map[new[2]], color_map[new[1]], color_map[new[0]])
    # print('{} {} {}'.format(new_str, old_str, new_str < old_str))
    return new_str < old_str

def cal(data, colors, cache, num):
    if cache[num].get(colors[0]):
        return cache[num].get(colors[0])
    summ = 0
    for x in range(0, len(data)):
        if x != num:
            summ += data[x][colors[0]]
    cache[num][colors[0]] = summ
    return summ

def main():
    start_time = time.time()
    for line in sys.stdin:
        cache = {}
        b = line.split()
        b = list(map(lambda x: int(x), b))
        data = []
        colors = [0, 1, 2]
        for group in range(0, len(colors)):
            start = 3*group
            end = 3*(group+1)
            data.append(b[start:end])
            cache[group] = {}
        # x_pre_result = process(data, colors, cache)
        # for pre_result in x_pre_result:
        #     print('{}{}{} {}'.format(color_map[pre_result['route'][2]], color_map[pre_result['route'][1]], color_map[pre_result['route'][0]], pre_result['value']))

        pre_result = process(data, colors, cache)[0]
        print('{}{}{} {}'.format(color_map[pre_result['route'][2]], color_map[pre_result['route'][1]], color_map[pre_result['route'][0]], pre_result['value']))

    # print("--- %s seconds ---" % (time.time() - start_time))

main()
