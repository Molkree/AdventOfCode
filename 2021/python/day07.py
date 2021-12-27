from statistics import mean, median

from utils import get_input_path

with open(get_input_path(7)) as f:
    crabs = [int(pos) for pos in f.readline().split(",")]

# Part 1
align_point = int(median(crabs))
fuel = sum(abs(crab - align_point) for crab in crabs)
assert fuel == 339321

# Part 2
mean_point = mean(crabs)
mean_low, mean_high = int(mean_point), int(mean_point + 1)


def calc_all_fuel(align_point: int) -> int:
    def calc_fuel(dist: int) -> int:
        return sum(range(1, dist + 1))

    return sum(calc_fuel(abs(crab - align_point)) for crab in crabs)


fuel_low = calc_all_fuel(mean_low)
fuel_high = calc_all_fuel(mean_high)
fuel = min(fuel_low, fuel_high)
assert fuel == 95476244
