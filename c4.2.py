import functools
from aoc_io import get_input

def aoc(input):
    return ( # L1
        functools.reduce(
            lambda res, number: res if not len(res[0]) else ( # L Reduce: if tere is no more board the result is the one of the last wining board
                lambda boards, is_winning, winning_board: ( # L1
                    [board for board in boards if not is_winning(board)], winning_board(boards, is_winning)[0] * number)  # Step 2 Filter Wining board
                )( # Args L1
                    [[(v, 1) if v == number else (v, m) for v, m in board]  for board in res[0]], # Step 1: Mark board
                    lambda board: any([ all([board[pos][1] for pos in range(len(board)) if pos // 5 == i]) or all ([board[pos][1] for pos in range(len(board)) if pos % 5 == i]) for i in range(5)]), # Check if board is winning
                    lambda boards, is_winning: [sum([v for v, m in board if m == 0])  for board in boards if is_winning(board)][:1] or [0], # sum of winning board
                ),
            list(map(int, input[0].split(","))), # List to reduce: bingo number
            ([[(v, 0) for v in list(map(int, " ".join(input[1:][i:i+5]).strip().replace("  ", " ").split(" ")))] for i in range(len(input[1:])) if i % 5 == 0], False), # Initial Board
        ))[1]

test = ["7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
"22 13 17 11  0",
" 8  2 23  4 24",
"21  9 14 16  7",
" 6 10  3 18  5",
" 1 12 20 15 19",

" 3 15  0  2 22",
" 9 18 13 17  5",
"19  8  7 25 23",
"20 11 10 24  4",
"14 21 16 12  6",

"14 21 17 24  4",
"10 16 15  9 19",
"18  8 23 26 20",
"22 11 13  6  5",
" 2  0 12  3  7",
]
print(aoc(test))
print(aoc(get_input(4)))
