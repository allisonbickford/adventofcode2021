from typing import List
from functools import reduce

# count the number of times a depth measurement increases 
# from the previous measurement.
# (There is no measurement before the first measurement.)
def part_1(inputs: List[int]) -> int:
    increases = 0
    previous_measurement = None
    for item in inputs:
        if previous_measurement is not None and previous_measurement < item:
            increases += 1

        previous_measurement = item

    return increases


# Your goal now is to count the number of times the sum of measurements 
# in this sliding window increases from the previous sum. So, compare A
#  with B, then compare B with C, then C with D, and so on. Stop when
# there aren't enough measurements left to create a new three-measurement
# sum.
def part_2(inputs: List[int]) -> int:
    count = 0
    current_window = []
    previous_window = []

    for item in inputs:
        if len(current_window) == 3:
            current_window.pop(0)
        current_window.append(item)     

        if len(previous_window) == 3 and len(current_window) == 3:
            current_sum = reduce(lambda a, b: a+b, current_window)
            previous_sum = reduce(lambda a, b: a+b, previous_window)
            if current_sum > previous_sum:
                count += 1

        if len(previous_window) == 3:
            previous_window.pop(0)
        previous_window.append(item)

    return count

if __name__ == "__main__":
    with open("./day_1_actual.txt", "r") as data:
        inputs = data.read().split("\n")
        inputs = [int(item) for item in inputs]
        # print('using inputs', inputs)
        print(part_1(inputs))
        print(part_2(inputs))