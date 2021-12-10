import functools
from aoc_io import get_input

def aoc(input):
    return (lambda token_state, closing, score_map: 
        (lambda sane_line, score: sorted([score(l) for l in sane_line])[len(sane_line) // 2])( # Find the score and take the middle one
            [l[1] for l in [token_state(i, closing) for i in input] if not l[0] ], # Filter token list based on their state
            lambda l: functools.reduce( # Compute score based on token not closed
                lambda acc, c: acc * 5 + score_map[c],
                l[::-1],
                0,
            )
        )
    )(
        lambda i, closing: functools.reduce( # Return token state, corrupted or not and the token not closed
            lambda a, c: a if a[0] else (
                (a[0], a[1] + [c]) if c in closing.keys() else (
                    (True, a[1]) if closing[a[1][-1]] != c else (a[0], a[1][:-1])
                )
            ),
            i,
            (False, [])
        ),
        {
            '(' : ')',
            '{' : '}',
            '[' : ']',
            '<' : '>',
        },
        {
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4,
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
