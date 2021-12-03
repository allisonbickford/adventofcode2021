from typing import List

# count the number of times a depth measurement increases 
# from the previous measurement.
# (There is no measurement before the first measurement.)
def amount_of_increases(inputs: List[str]):
    increases = 0
    previous_measurement = None
    for input in inputs:
        if previous_measurement is not None and previous_measurement < input:
            increases += 1

        previous_measurement = input

    return increases

if __name__ == "__main__":
    with open("./day_1_actual.txt", "r") as data:
        inputs = data.read().split("\n")
        inputs = [int(item) for item in inputs]
        # print('using inputs', inputs)
        print(amount_of_increases(inputs))