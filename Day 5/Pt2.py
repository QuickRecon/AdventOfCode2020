import math


def get_component_recursive(seat_string, seat_set, upper_char, lower_char):
    if len(seat_string) == 1:
        if seat_string == lower_char:
            return seat_set[0]
        elif seat_string == upper_char:
            return seat_set[0]+1

    curr_char = seat_string[0]
    seat_string = seat_string[1:len(seat_string)]
    lower_set = seat_set[0:math.ceil(len(seat_set) / 2)]
    upper_set = seat_set[math.ceil(len(seat_set) / 2):len(seat_set)]
    if curr_char == lower_char:
        return get_component_recursive(seat_string, lower_set, upper_char, lower_char)
    elif curr_char == upper_char:
        return get_component_recursive(seat_string, upper_set, upper_char, lower_char)

inputFile = open("input", "r")

lines = inputFile.readlines()


seatSet = [8*get_component_recursive(line[0:7], range(0, 127), 'B', 'F') + get_component_recursive(line[7:10], range(0, 7), 'R', 'L') for line in lines]

candidates = [element for element in range(0, max(seatSet)) if element not in seatSet]

print(max(candidates))