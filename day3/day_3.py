from typing import List, Tuple
from functools import reduce



# Each bit in the gamma rate can be determined by finding the most common bit
#  in the corresponding position of all numbers in the diagnostic report.
# The epsilon rate is calculated in a similar way; rather than use the 
# most common bit, the least common bit from each position is used.
def part_1(inputs: List[str]) -> Tuple[str, str]:
    """
    @returns gamma, epsilon
    """
    gamma = ""
    epsilon = ""

    amount_of_bits = len(inputs[0])
    for bit in range(0, amount_of_bits):
        amount_of_ones = 0
        amount_of_zeroes = 0

        print(f'looking at position {bit}')

        for binary_number in inputs:
            if binary_number[bit] == "1":
                amount_of_ones += 1
            else:
                amount_of_zeroes += 1

        print(f'we have {amount_of_zeroes} 0s and {amount_of_ones} 1s')
        if amount_of_zeroes > amount_of_ones:
            gamma = f"{gamma}0"
            epsilon = f"{epsilon}1"
        else:
            gamma = f"{gamma}1"
            epsilon = f"{epsilon}0"
        print(f'gamma is {gamma}, epsilon is {epsilon}')
        
    return gamma, epsilon


def part_2(inputs: List[str]) -> Tuple[str, str]:
    """
    To find oxygen generator rating, determine the most common value (0 or 1)
    in the current bit position, and keep only numbers with that bit in that position.
    If 0 and 1 are equally common, keep values with a 1 in the position being considered.
    
    To find CO2 scrubber rating, determine the least common value (0 or 1) in the current
    bit position, and keep only numbers with that bit in that position. If 0 and 1
    are equally common, keep values with a 0 in the position being considered.
    @returns oxygen_rating, co2_rating
    """
    oxygen_rating = get_most_common_bits(inputs, False)
    co2_rating = get_most_common_bits(inputs, True)

    return oxygen_rating, co2_rating


def get_most_common_bits(inputs: List[str], reversed: bool) -> str:
    result = ""
    candidates = list(range(len(inputs)))

    print(reversed)

    amount_of_bits = len(inputs[0])
    for bit in range(0, amount_of_bits):
        if len(candidates) == 1:
            break

        amount_of_ones = 0
        amount_of_zeroes = 0

        print(f'~~~~~ {bit} ~~~~')

        index = 0
        for binary_number in inputs:
            if len(candidates) == 1:
                break

            if not binary_number.startswith(result):
                if index in candidates:
                    print(f"  removing {index} from {candidates}")
                    candidates.remove(index)
                index += 1
                continue

            if binary_number[bit] == "1":
                amount_of_ones += 1
            else:
                amount_of_zeroes += 1
            
            index += 1

        print(f'  {amount_of_zeroes} 0s ... {amount_of_ones} 1s')
        print(f'  candidates = {candidates}')
        if reversed:
            if amount_of_ones < amount_of_zeroes:
                result = f"{result}1"
            else:
                result = f"{result}0"
        else:
            if amount_of_zeroes > amount_of_ones:
                result = f"{result}0"
            else:
                result = f"{result}1"
        print(f'  {result}')

    return inputs[candidates[0]]


if __name__ == "__main__":
    with open("./day_3.txt", "r") as data:
        inputs = data.read().split("\n")
        # gamma, epsilon = part_1(inputs)
        # print('gamma =', gamma, 'epsilon =', epsilon)
        # print('gamma =', int(gamma, 2), 'epsilon =', int(epsilon, 2))
        # print('multiplied:', int(gamma, 2) * int(epsilon, 2))

        oxygen, co2 = part_2(inputs)
        print(f"oxygen = {oxygen}, co2 = {co2}")
        print('oxygen =', int(oxygen, 2), 'co2 =', int(co2, 2))
        print('multiplied:', int(oxygen, 2) * int(co2, 2))