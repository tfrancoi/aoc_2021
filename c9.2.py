import functools
from aoc_io import get_input

def aoc(input):
    return (lambda map_height, max_x, max_y, adjacent: (
                lambda browse, low_point: functools.reduce( # Find the 3 max
                    lambda cpt, cur: (
                        cpt[0] * max(cpt[1]),
                        [b for i, b in enumerate(cpt[1]) if i != cpt[1].index(max(cpt[1]))]
                    ),
                    range(3),
                    (1, [len(s) for s in ( # find the bassin of each low point
                        lambda low_point: [browse(set(), pos, h)  for pos, h in low_point])(low_point)
                    ])
                )[0]
            )(
            lambda visited, pos, h: ( # Find bassin from a low point
                lambda browse: browse(browse, visited, pos, h)
            )(
                lambda browse, visited, pos, h: set().union(*([visited, {pos}] + [
                    browse(browse, visited | {p}, p, map_height[p]) for p in adjacent(pos, max_x, max_y) 
                    if p not in visited and map_height[p] > h and map_height[p] < 9
                ]))
            ),
            [cur for cur in map_height.items() if all([map_height[p] > cur[1] for p in adjacent(cur[0], max_x, max_y)])],
        ))(
            {(x,y): int(h) for y, l in enumerate(input) for x, h in enumerate(l)},
            len(input[0]),
            len(input),
            lambda pos, max_x, max_y: ( # Get adjacent point
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
