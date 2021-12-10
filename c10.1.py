import functools
from aoc_io import get_input

def aoc(input):
    return (lambda closing, score: functools.reduce(
        lambda acc, i: acc + functools.reduce(
            lambda a, c: a if a[2] else (
                (a[0], a[1] + [c], a[2]) if c in closing.keys() else (
                    (score[c], a[1], True) if closing[a[1][-1]] != c else (a[0], a[1][:-1], a[2])
                )
            ),
            i,
            (0, [], False)
        )[0],
        input,
        0,
    ))(
        {
            '(' : ')',
            '{' : '}',
            '[' : ']',
            '<' : '>',
        },
        {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137,
        }
    )


test = [
'[({(<(())[]>[[{[]{<()<>>',
'[(()[<>])]({[<{<<[]>>(',
'{([(<{}[<>[]}>{[]{[(<()>',
'(((({<>}<{<{<>}{[]{[]{}',
'[[<[([]))<([[{}[[()]]]',
'[{[{({}]{}}([{[{{{}}([]',
'{<[[]]>}<{[{[{[]{()[[[]',
'[<(<(<(<{}))><([]([]()',
'<{([([[(<>()){}]>(<<{{',
'<{([{{}}[<[[[<>{}]]]>[]]',
]

print(aoc(test))
print(aoc(get_input(10)))
