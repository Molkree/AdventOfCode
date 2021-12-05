from utils import get_input_path

day = 5
print(f"Day {day:02}")


def partition(
    seat_string: str,
    upper_bound: int,
    lower_half_char: str,
    iterations: int,
    string_start_position: int = 0,
) -> int:
    lower_bound = 0
    for i in range(string_start_position, string_start_position + iterations):
        middle = lower_bound + (upper_bound - lower_bound) // 2
        if seat_string[i] == lower_half_char:
            upper_bound = middle
        else:
            lower_bound = middle + 1
    return lower_bound


def get_seat_id(seat_string: str) -> int:
    row = partition(seat_string, 127, "F", 7)
    column = partition(seat_string, 7, "L", 3, 7)
    return row * 8 + column


with open(get_input_path(day)) as f:
    lines = f.readlines()
seat_ids = [get_seat_id(seat) for seat in lines]
seat_ids.sort()
my_seat = 0
for i in range(0, len(seat_ids)):
    if seat_ids[i + 1] != seat_ids[i] + 1:
        my_seat = seat_ids[i] + 1
        break

print(f"Part 1: {seat_ids[-1]}")
print(f"Part 2: {my_seat}")
