import functools
from aoc_io import get_input

def aoc(input):
    return (lambda res: res[0]*res[1])(functools.reduce(
        lambda counter, cur: (
            lambda counter, cur, matrix: (counter[0] + matrix[0] * int(cur[1]), counter[1] + matrix[1] * int(cur[1])))(
                counter, cur, {'up': (-1, 0), 'down': (1, 0), 'forward': (0, 1)}[cur[0]]),
        [pos.split() for pos in input],
        (0, 0)
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
