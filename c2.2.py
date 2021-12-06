import functools
from aoc_io import get_input

def aoc(input):
    return (lambda res: res[1]*res[0])(functools.reduce(
        lambda counter, cur: (
            lambda counter, cur, matrix: (counter[0] + matrix[0] * int(cur[1]) * counter[2], counter[1] + matrix[1] * int(cur[1]), counter[2] + matrix[2] * int(cur[1])))(
                counter, cur, {'up': (0, 0, -1), 'down': (0, 0, 1), 'forward': (1, 1, 0)}[cur[0]]),
        [pos.split() for pos in input],
        (0, 0, 0)
    ))

test = [
'forward 5',
'down 5',
'forward 8',
'up 3',
'down 8',
'forward 2',
]
print(aoc(test))
print(aoc(get_input(2)))
