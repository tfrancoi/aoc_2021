import functools
from aoc_io import get_input

def aoc(input):
    return (lambda to_int, b1, b2: to_int(b1) * to_int(b2))(  # Multiply int
        lambda b: int('0b'+''.join([str(i) for i in b]), 2),  # Binary to int
        *(lambda b_list: (b_list, [1 - b for b in b_list]))(  # Take the complementary
            [0 if current[0] > current[1] else 1 for current in functools.reduce(  # Choose most common bit
                    lambda counter, cur: [[counter[i][0] + 1 - int(pos), counter[i][1] + int(pos)] for i, pos in enumerate(cur)],  # Count bit
                    input,
                    [[0,0] for _ in range(len(input[0]))] # Initialize counter
                )
            ]
        )
    )


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
