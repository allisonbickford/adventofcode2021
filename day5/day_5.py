from typing import List, Tuple
from collections import Counter
import time


def part_1(lines: List[str]) -> int:
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

    items = []
    for line in lines:
        pieces = line.split(' -> ')
        start = pieces[0].split(',')
        start_x = int(start[0])
        start_y = int(start[1])
        
        end = pieces[1].split(',')
        end_x = int(end[0])
        end_y = int(end[1])

        # Uncomment for part 1, comment for part 2
        # if start_x != end_x and start_y != end_y:
        #     continue

        current_x = start_x
        current_y = start_y
        # print(f'start ({current_x}, {current_y})')

        while current_x != end_x or current_y != end_y:

            items.append((current_x, current_y))

            if current_x > end_x:
                current_x -= 1
            elif current_x < end_x:
                current_x += 1

            if current_y > end_y:
                current_y -= 1
            elif current_y < end_y:
                current_y += 1

            # print(f'\t{current_x} \t {current_y}')

        items.append((end_x, end_y))
        # print(f'end ({end_x}, {end_y})')


    count = Counter(items)
    # print([item for item in count.items() if item[1] > 1])

    return len([item for item in count.items() if item[1] > 1])


def part_2(called_numbers: List[int], board_lines: List[str]) -> int:
    
    return 0


if __name__ == "__main__":
    start = time.time()

    inputs = []
    with open("./day_5.txt", "r") as data:
        inputs = data.readlines()
        # print(inputs)
        result = part_1(inputs)
        print(result)

    print(time.time() - start)