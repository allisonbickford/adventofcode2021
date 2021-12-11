from typing import List, Tuple
from collections import Counter
import time


def parse_fish(fishes: List[int], days_left: int):
    print(f"Day {days_left}")
    print(f"\t{len(fishes)}")
    if days_left == 0:
        return len(fishes)

    result = []
    for fish in fishes:
        if fish == 0:
            result.append(8)
            result.append(6)
        else:
            result.append(fish - 1)
    
    return parse_fish(result, days_left - 1)


def part_1(numbers: List[int]) -> int:
    result = parse_fish(numbers, 256)
    print(result)

    return result


def part_2(numbers: List[int]) -> int:
    rev_list = list(reversed(range(9)))

    nums_ = [0] * 9
    for value in numbers:
        nums_[value] += 1
    
    for day in range(256):
        new_nums = [0] * 9
        for index in rev_list:
            if nums_[index] > 0:
                if index == 0:
                    new_nums[8] += 1 * nums_[index]
                    new_nums[6] += nums_[index]
                if index - 1 >= 0:
                    new_nums[index - 1] = nums_[index]

        nums_ = new_nums

    return sum(nums_)


if __name__ == "__main__":
    start = time.time()

    inputs = []
    with open("./day_6.txt", "r") as data:
        inputs = data.readline()

        numbers = [int(item) for item in inputs.split(',')]
        # print(inputs)
        result = part_2(numbers)
        print(result)

    print(time.time() - start)
