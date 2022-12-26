from __future__ import annotations

import re
from collections import deque
from collections.abc import Generator
from dataclasses import dataclass
from pathlib import Path

from utils import get_input_path


@dataclass(frozen=True)
class Node:
    name: str
    rate: int


def find_paths(edges: dict[Node, list[Node]], goal: Node) -> dict[Node, int]:
    paths = {goal: 0}
    queue = deque([goal])
    while queue:
        current = queue.popleft()
        for neighbor in edges[current]:
            if neighbor not in paths:
                paths[neighbor] = paths[current] + 1
                queue.append(neighbor)
    return paths


def find_all_paths(
    edges: dict[Node, list[Node]], start_node: Node
) -> dict[Node, dict[Node, int]]:
    all_paths = {
        node: find_paths(edges, node)
        for node in edges
        if node.rate or node is start_node
    }
    for node, node_paths in all_paths.items():
        all_paths[node] = {
            other_node: cost
            for other_node, cost in node_paths.items()
            if other_node.rate
        }
    return all_paths


def parse_input(path: Path) -> tuple[Node, dict[Node, dict[Node, int]]]:
    nodes: dict[str, Node] = {}
    edges_str: dict[Node, list[str]] = {}
    with open(path) as f:
        for line in f:
            match = re.search(
                "Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)", line
            )
            if match:
                name, rate, neighbors = match.groups()
                nodes[name] = node = Node(name, int(rate))
                edges_str[node] = neighbors.split(", ")

    edges = {
        node: [nodes[neighbor] for neighbor in neighbors]
        for node, neighbors in edges_str.items()
    }

    start_node = nodes["AA"]
    return start_node, find_all_paths(edges, start_node)


start_node, distances = parse_input(get_input_path(16))
for node, node_distances in distances.items():
    print(node.name, node_distances.values())
working_nodes = {node for node in distances if node.rate}


def all_orders(
    distances: dict[Node, dict[Node, int]],
    node: Node,
    todo: set[Node],
    done: list[Node],
    time_limit: int,
) -> Generator[list[Node], None, None]:
    for next_node in todo:
        cost = distances[node][next_node] + 1
        if cost < time_limit:
            yield from all_orders(
                distances,
                next_node,
                todo - {next_node},
                done + [next_node],
                time_limit - cost,
            )
    yield done


orders = all_orders(distances, start_node, working_nodes, [], 30)


def run_order(
    costs: dict[Node, dict[Node, int]], start_node: Node, nodes: list[Node], time: int
) -> int:
    released_pressure = 0
    current = start_node
    for node in nodes:
        cost = costs[current][node] + 1
        time -= cost
        released_pressure += time * node.rate
        current = node
    return released_pressure


max_released_pressure = max(
    run_order(distances, start_node, order, 30) for order in orders
)
assert max_released_pressure == 2080
