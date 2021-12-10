import functools
from aoc_io import get_input

def aoc(input):
    return (lambda map_height, max_x, max_y, adjacent: functools.reduce(
            lambda answer, cur: answer + cur[1] + 1 if all([map_height[p] > cur[1] for p in adjacent(cur[0], max_x, max_y)]) else answer,
            map_height.items(),
            0,
        ) 
    )(
        {(x,y): int(h) for y, l in enumerate(input) for x, h in enumerate(l)},
        len(input[0]),
        len(input),
        lambda pos, max_x, max_y: (
            [(pos[0] + tr, pos[1]) for tr in [-1, 1] if 0 <= pos[0] + tr < max_x] +
            [(pos[0], pos[1] + tr) for tr in [-1, 1] if 0 <= pos[1] + tr < max_y]
        )
    )

test = [
'2199943210',
'3987894921',
'9856789892',
'8767896789',
'9899965678',
]

print(aoc(test))
print(aoc(get_input(9)))
