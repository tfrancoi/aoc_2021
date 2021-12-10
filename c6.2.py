import functools
from aoc_io import get_input
from collections import Counter

def aoc(input):
    return sum(functools.reduce(
        lambda fish, cur: dict(
            {str(int(k)-1) : v  for k, v in fish.items() if int(k) > 0}, 
            **{'8': fish.get('0', 0)}, 
            **{'6': fish.get('7', 0) + fish.get('0', 0)}),
        range(256),
        {str(k): v for k, v in Counter(list(map(int, input[0].split(',')))).items() },
    ).values())

test = [
'3,4,3,1,2',
]
print(aoc(test))
print(aoc(get_input(6)))
