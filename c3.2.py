import functools
from aoc_io import get_input

def aoc(input):
    return (lambda input_data, to_int, loop, find_max_bit, filtered, up, low: to_int(loop(input_data, find_max_bit, filtered, up)) * to_int(loop(input_data, find_max_bit, filtered, low)))(
        input,
        lambda b: int('0b'+''.join([str(i) for i in b]), 2),
        lambda input_data, find_max_bit, filtered, f: (
                lambda l, input_data, pos: l(l, input_data, pos))(
                    lambda l, data, pos: data[0] if len(data) == 1 else l(l, filtered(data, pos, find_max_bit(data, pos, f)), pos+1 ),
                    input_data, 0),
        lambda data, pos, f: f(pos, functools.reduce(  # Choose most common bit
                    lambda counter, cur: [[counter[i][0] + 1 - int(pos), counter[i][1] + int(pos)] for i, pos in enumerate(cur)],  # Count bit
                    data,
                    [[0,0] for _ in range(len(data[0]))] # Initialize counter
                )),
        lambda data, pos, bit: [d for d in data if int(d[pos]) == bit],
        lambda pos, res: 1 if res[pos][0] <= res[pos][1] else 0,
        lambda pos, res: 0 if res[pos][0] <= res[pos][1] else 1)

test = [
'00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010',
]
print(aoc(test))
print(aoc(get_input(3)))

