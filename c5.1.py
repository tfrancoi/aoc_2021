import functools
from aoc_io import get_input

def aoc(input):
    return len([v for k, v in functools.reduce(
        lambda wind_map, seg: dict(wind_map, **{
            "%s, %s" % (i, j): wind_map.get("%s, %s" % (i, j), 0) + 1
            for i in range(min(seg[0][0], seg[1][0]), max(seg[0][0], seg[1][0]) + 1)
            for j in range(min(seg[0][1], seg[1][1]), max(seg[0][1], seg[1][1]) + 1)
            if min(seg[0][0], seg[1][0]) <= i <= max(seg[0][0], seg[1][0]) and min(seg[0][1], seg[1][1]) <= j <= max(seg[0][1], seg[1][1])
        }),
        list(filter(
            lambda seg: seg[0][0] == seg[1][0] or seg[0][1] == seg[1][1],
            [[tuple(map(int, p.split(','))) for p in l.split(" -> ")] for l in input]
        )),
        {},
    ).items() if v > 1])


test = [
'0,9 -> 5,9',
'8,0 -> 0,8',
'9,4 -> 3,4',
'2,2 -> 2,1',
'7,0 -> 7,4',
'6,4 -> 2,0',
'0,9 -> 2,9',
'3,4 -> 1,4',
'0,0 -> 8,8',
'5,5 -> 8,2',
]
print(aoc(test))
print(aoc(get_input(5)))
