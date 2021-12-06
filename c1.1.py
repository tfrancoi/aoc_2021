import functools
import sys
from aoc_io import get_input

def aoc(input):
    return functools.reduce(
        lambda t, cur: (cur, t[1] + 1) if cur > t[0] else (cur, t[1]),
        map(int, input),
        (sys.maxsize, 0)
    )[1]

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
