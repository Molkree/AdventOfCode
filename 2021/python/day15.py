import heapq as hq
from math import inf

from utils import get_input_path

with open(get_input_path(15)) as f:
    lines = f.readlines()

grid = [[int(node) for node in line.rstrip()] for line in lines]


class Vertex:
    def __init__(self, weight: int) -> None:
        self.weight = weight
        self.neighbors = list[int]()


def build_graph() -> list[Vertex | None]:
    graph: list[Vertex | None] = [Vertex(node) for row in grid for node in row]
    height, width = len(grid), len(grid[0])
    ind = 0
    for row in range(height):
        for col in range(width):
            if row > 0:
                graph[ind].neighbors.append(ind - width)  # type:ignore
            if row < height - 1:
                graph[ind].neighbors.append(ind + width)  # type:ignore
            if col > 0:
                graph[ind].neighbors.append(ind - 1)  # type:ignore
            if col < width - 1:
                graph[ind].neighbors.append(ind + 1)  # type:ignore
            ind += 1
    return graph


graph = build_graph()


def dijkstra() -> int:
    node_count = len(graph)
    weights = [inf] * node_count
    queue = list[tuple[float, int]]()
    hq.heappush(queue, (0, 0))
    while queue:
        distance, node_ind = hq.heappop(queue)
        if node_ind == node_count - 1:
            break
        for neighbor_ind in graph[node_ind].neighbors:  # type:ignore
            if graph[neighbor_ind]:
                new_distance = distance + graph[neighbor_ind].weight  # type:ignore
                if new_distance < weights[neighbor_ind]:
                    weights[neighbor_ind] = new_distance
                    hq.heappush(queue, (new_distance, neighbor_ind))
        graph[node_ind] = None
    return int(weights[-1])


assert dijkstra() == 393

old_height, old_width = len(grid), len(grid[0])
for line in grid:
    for i in range(1, 5):
        new_line = list[int]()
        for node in line[:old_width]:
            new_node = node + i
            if new_node > 9:
                new_node = new_node % 10 + 1
            new_line.append(new_node)
        line += new_line

for i in range(1, 5):
    for row in range(old_height):
        new_line = list[int]()
        for col in range(len(grid[0])):
            new_node = grid[row][col] + i
            if new_node > 9:
                new_node = new_node % 10 + 1
            new_line.append(new_node)
        grid.append(new_line)
graph = build_graph()
assert dijkstra() == 2823
# Part 2 is kinda slow and takes ~1s on my laptop...
# Using a flat list of [weight, *neighbors] instead of Vertex only speeds it up
# to ~0.6-0.8s so I'm keeping the class for readability
