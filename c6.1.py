import functools
from aoc_io import get_input

def aoc(input):
    return len(functools.reduce(
        lambda fish, cur: [i - 1 if i > 0 else 6 for i in fish] + fish.count(0) * [8],
        range(80),
        list(map(int, input[0].split(','))),
    ))

test = [
'3,4,3,1,2',
]
print(aoc(test))
print(aoc(get_input(6)))
