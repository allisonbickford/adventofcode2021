from typing import List, Tuple
from functools import reduce


# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.
# Calculate the horizontal position and depth you would have after following the planned course
def part_1(inputs: List[int]) -> Tuple[int, int]:
    horizontal = 0
    depth = 0

    for item in inputs:
        instructions = item.split(" ")
        direction = instructions[0]
        amount = int(instructions[1])

        if direction == "forward":
            horizontal += amount
        elif direction == "up":
            depth -= amount
        elif direction == "down":
            depth += amount
        
    return horizontal, depth


# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
#     It increases your horizontal position by X units.
#     It increases your depth by your aim multiplied by X.
# What do you get if you multiply your final horizontal position by your final depth?
def part_2(inputs: List[int]) -> Tuple[int, int, int]:
    horizontal = 0
    depth = 0
    aim = 0

    for item in inputs:
        instructions = item.split(" ")
        direction = instructions[0]
        amount = int(instructions[1])

        if direction == "forward":
            horizontal += amount
            depth += (aim * amount)
        elif direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount
        
    return horizontal, depth, aim

if __name__ == "__main__":
    with open("./day_2.txt", "r") as data:
        inputs = data.read().split("\n")
        # horizontal, depth = part_1(inputs)
        # print(horizontal, depth)
        # print('multiplied:', horizontal * depth)

        horizontal_2, depth_2, aim = part_2(inputs)
        print(horizontal_2, depth_2)
        print('multiplied:', horizontal_2 * depth_2)