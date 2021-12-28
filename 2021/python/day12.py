from collections import defaultdict
from functools import cache

from utils import get_input_path

with open(get_input_path(12)) as f:
    edges = f.readlines()
graph = defaultdict[str, set[str]](set)
for edge in edges:
    start, end = edge.split("-")
    end = end.rstrip()
    graph[start].add(end)
    graph[end].add(start)


@cache
def count_paths(
    node: str = "start",
    visited: frozenset[str] = frozenset[str](),
    allow_2visit: bool = False,
) -> int:
    if node.islower():
        visited |= {node}
    count = 0
    for neighbor in graph[node]:
        if neighbor == "end":
            count += 1
        elif neighbor not in visited:
            count += count_paths(neighbor, visited, allow_2visit)
        elif allow_2visit and neighbor != "start":
            count += count_paths(neighbor, visited, False)
    return count


assert count_paths() == 4720
assert count_paths(allow_2visit=True) == 147848
