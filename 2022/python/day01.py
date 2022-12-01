import heapq

from utils import get_input_path

with open(get_input_path(1)) as f:
    top_elves = [0, 0, 0]
    calories = int(f.readline())
    for line in f:
        if line == "\n":
            heapq.heappushpop(top_elves, calories)
            calories = 0
            continue
        calories += int(line)
    heapq.heappushpop(top_elves, calories)
assert max(top_elves) == 67633
assert sum(top_elves) == 199628
