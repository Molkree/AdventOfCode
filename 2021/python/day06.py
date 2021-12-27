from collections import deque

from utils import get_input_path

with open(get_input_path(6)) as f:
    fish = deque([0] * 7)
    for str_fish in f.readline().split(","):
        fish[int(str_fish)] += 1
new_fish = [0] * 2


def step() -> None:
    grown_fish = new_fish[0]
    new_fish[0] = new_fish[1]
    new_fish[1] = fish[0]
    fish.rotate(-1)
    fish[-1] += grown_fish


for _ in range(80):
    step()
assert sum(fish) + sum(new_fish) == 351188
for _ in range(256 - 80):
    step()
assert sum(fish) + sum(new_fish) == 1595779846729
