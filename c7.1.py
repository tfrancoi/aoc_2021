import functools
from aoc_io import get_input
from collections import Counter

def aoc(input):
    return min((lambda input_data, cost: 
        [sum([cost(abs(i - p)) for i in input_data]) for p in range(max(input_data))]
    )(
        list(map(int, input[0].split(","))),
        lambda x: x,
    ))

test = [
"16,1,2,0,4,2,7,1,2,14"
]

print(aoc(test))
print(aoc(get_input(7)))
