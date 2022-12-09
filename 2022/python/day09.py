from utils import get_input_path

with open(get_input_path(9)) as f:
    moves = f.read().splitlines()


tails_count = 9
knots: list[tuple[int, int]] = [(0, 0)] * (tails_count + 1)
visited: list[set[tuple[int, int]]] = [{(0, 0)} for _ in range(tails_count)]


def shift(prev_coord: int, next_coord: int) -> int:
    if prev_coord > next_coord:
        return 1
    if prev_coord < next_coord:
        return -1
    return 0


def move_tails(
    tails_count: int, knots: list[tuple[int, int]], visited: list[set[tuple[int, int]]]
) -> None:
    for i in range(1, tails_count + 1):
        (x1, y1), (x2, y2) = knots[i - 1], knots[i]
        if abs(x1 - x2) < 2 and abs(y1 - y2) < 2:
            break
        knots[i] = x2 + shift(x1, x2), y2 + shift(y1, y2)
        visited[i - 1].add(knots[i])


for move in moves:
    direction, distance = move[0], int(move[2:])
    for _ in range(distance):
        if direction == "U":
            knots[0] = knots[0][0], knots[0][1] + 1
        if direction == "D":
            knots[0] = knots[0][0], knots[0][1] - 1
        if direction == "R":
            knots[0] = knots[0][0] + 1, knots[0][1]
        if direction == "L":
            knots[0] = knots[0][0] - 1, knots[0][1]
        move_tails(tails_count, knots, visited)

assert len(visited[0]) == 6357
assert len(visited[-1]) == 2627
