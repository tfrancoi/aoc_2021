import functools
import sys
from aoc_io import get_input

def aoc(input):
    return (lambda input_list: functools.reduce(
        lambda t, cur: (cur, t[1] + 1) if sum(cur) > sum(t[0]) else (cur, t[1]),
        [input_list[i-2:i+1] for i, value in enumerate(input_list) if i > 1],
        ([sys.maxsize, 0, 0], 0)
    )[1])(list(map(int, input)))

test = [
'199',
'200',
'208',
'210',
'200',
'207',
'240',
'269',
'260',
'263',
]
print(aoc(test))
print(aoc(get_input(1)))
