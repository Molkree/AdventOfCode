from utils import get_input_path

with open(get_input_path(9)) as f:
    moves = f.read().splitlines()

head_pos = 0, 0
tail_pos = 0, 0
visited: set[tuple[int, int]] = {tail_pos}
for move in moves:
    direction, distance = move[0], int(move[2:])
    if direction == "U":
        head_pos = head_pos[0], head_pos[1] + distance
        for y in range(tail_pos[1] + 1, head_pos[1]):
            tail_pos = head_pos[0], y
            visited.add(tail_pos)
    elif direction == "D":
        head_pos = head_pos[0], head_pos[1] - distance
        for y in range(tail_pos[1] - 1, head_pos[1], -1):
            tail_pos = head_pos[0], y
            visited.add(tail_pos)
    elif direction == "R":
        head_pos = head_pos[0] + distance, head_pos[1]
        for x in range(tail_pos[0] + 1, head_pos[0]):
            tail_pos = x, head_pos[1]
            visited.add(tail_pos)
    elif direction == "L":
        head_pos = head_pos[0] - distance, head_pos[1]
        for x in range(tail_pos[0] - 1, head_pos[0], -1):
            tail_pos = x, head_pos[1]
            visited.add(tail_pos)
assert len(visited) == 6357
