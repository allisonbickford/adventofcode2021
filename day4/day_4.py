from typing import List, Tuple
from copy import deepcopy
import numpy as np
import time


def part_1(called_numbers: List[int], board_lines: List[str]) -> int:
    """
    Numbers are chosen at random, and the chosen number is marked
    on all boards on which it appears. (Numbers may not appear on
    all boards.) If all numbers in any row or any column of a board
    are marked, that board wins. (Diagonals don't count.)

    The score of the winning board can now be calculated. Start by
    finding the sum of all unmarked numbers on that board; in this
    case, the sum is 188. Then, multiply that sum by the number that
    was just called when the board won to get the final score.
    """
    board_size = len(board_lines[0].split(' '))
    boards = []
    winning_row = [-1 for item in range(board_size)]

    # setup board matricies
    index = 0
    while index < len(board_lines):
        if (index + board_size) > len(board_lines):
            break

        board = [
            [int(number) for number in line.split(' ')]
            for line in board_lines[index:(index + board_size)]
            ]
        # print(f'~~~~~ {index} ~~~~~~')
        # print(np.asarray(board, dtype='int'))
        boards.append(board)

        index += board_size

    # original_boards = deepcopy(boards)

    bingo = -1
    winning_number = 0
    for number in called_numbers:
        if bingo >= 0:
            break

        for index, board in enumerate(boards):
            if bingo >= 0:
                break

            updated_board = [[-1 if item == number else item for item in line] for line in board]
            boards[index] = updated_board

            # check rows
            for line in updated_board:
                if set(line) == set(winning_row):
                    bingo = index
                    # print('winning_number', number)

                    winning_number = number
                    break

            # check columns
            for col_index in range(board_size):
                # print('********************************')
                # print(set([line[col_index] for line in board]))
                # print(set([line[col_index] for line in board]) == set(winning_row))
                # print('********************************')
                if set([line[col_index] for line in updated_board]) == set(winning_row):
                    # print([item[col_index] for item in board])
                    bingo = index
                    # print('winning_number', number)
                    winning_number = number
                    break

    # print('----- winner ------')
    # print(np.asarray(original_boards[bingo]))

    # print('-------------------')
    # print(np.asarray(boards[bingo]))

    flattened_board = np.array(boards[bingo]).flatten().tolist()
    sum_of_unmarked_values = np.sum([item for item in flattened_board if item != -1])
    # print('sum', sum_of_unmarked_values)
    # print('winning', winning_number)
    # print('result', sum_of_unmarked_values * winning_number)

    return sum_of_unmarked_values * winning_number


def part_2(called_numbers: List[int], board_lines: List[str]) -> int:
    board_size = len(board_lines[0].split(' '))
    boards = []
    winning_row = [-1 for item in range(board_size)]

    # setup board matricies
    index = 0
    while index < len(board_lines):
        if (index + board_size) > len(board_lines):
            break

        board = [
            [int(number) for number in line.split(' ')]
            for line in board_lines[index:(index + board_size)]
            ]
        # print(f'~~~~~ {index} ~~~~~~')
        # print(np.asarray(board, dtype='int'))
        boards.append(board)

        index += board_size

    original_boards = deepcopy(boards)

    bingo = []
    winning_number = 0
    for number in called_numbers:
        if len(bingo) == len(boards):
            break

        for index, board in enumerate(boards):
            if len(bingo) == len(boards):
                break

            updated_board = [[-1 if item == number else item for item in line] for line in board]
            boards[index] = updated_board

            # check rows
            for line in updated_board:
                if set(line) == set(winning_row):
                    if index not in bingo:
                        bingo.append(index)
                    winning_number = number
                    break

            # check columns
            for col_index in range(board_size):
                # print('********************************')
                # print(set([line[col_index] for line in board]))
                # print(set([line[col_index] for line in board]) == set(winning_row))
                # print('********************************')
                if set([line[col_index] for line in updated_board]) == set(winning_row):
                    if index not in bingo:
                        bingo.append(index)
                    winning_number = number
                    break

    # print(bingo)
    last_winner_index = bingo[-1]
    # print(f'----- winner {last_winner_index} ------')
    # print(np.asarray(original_boards[last_winner_index]))

    # print('-------------------')
    # print(np.asarray(boards[last_winner_index]))

    flattened_board = np.array(boards[last_winner_index]).flatten().tolist()
    sum_of_unmarked_values = np.sum([item for item in flattened_board if item != -1])
    # print('sum', sum_of_unmarked_values)
    # print('winning', winning_number)
    # print('result', sum_of_unmarked_values * winning_number)

    return sum_of_unmarked_values * winning_number


if __name__ == "__main__":
    start = time.time()

    called_numbers = []
    inputs = []
    with open("./day_4.txt", "r") as data:
        called_numbers = [int(item) for item in data.readline().split(',')]
        inputs = [" ".join(line.strip().split()) for line in data.readlines()[1:] if line.strip()]
        # print(inputs)
        result = part_2(called_numbers, inputs)
        print(result)

    print(time.time() - start)