import functools
from aoc_io import get_input

def aoc(input):
    return (lambda get_pos, digits_map: (
        lambda to_int, filter_digit, to_pos, common: functools.reduce(
            lambda cpt, input_data: (cpt + (
                lambda digit_pos: to_int(
                    [digits_map[common(d, digit_pos)] for d in [to_pos(d) for d in input_data.split(' | ')[1].split(' ')]]
                ))(
                    filter_digit(input_data.split(' | ')[0].split(' '), to_pos)
                )
            ),
            input,
            0
        ))(
            lambda digit_list: int(''.join(digit_list)),
            lambda d_list, to_pos: {{2: 0, 4: 1, 3:2, 7:3}[len(d)]: to_pos(d) for d in d_list if len(d) in [2,4,3,7]},
            lambda digit: tuple([1 if any(get_pos[d] == i for d in digit) else 0 for i in range(7)]),
            lambda digit, digit_pos: tuple([sum([digit_pos[i][j] and digit[j] for j in range(7)]) for i in range(4)]),
    ))(
        {l: i for i, l in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g'])},
        {
            (2, 3, 3, 6): '0', 
            (2, 2, 2, 2): '1', 
            (1, 2, 2, 5): '2',
            (2, 3, 3, 5): '3', 
            (2, 4, 2, 4): '4', 
            (1, 3, 2, 5): '5',
            (1, 3, 2, 6): '6',
            (2, 2, 3, 3): '7', 
            (2, 4, 3, 7): '8',
            (2, 4, 3, 6): '9', 
        },
    )


test = [
'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce',

]


print(aoc(test))
print(aoc(get_input(8)))
