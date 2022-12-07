from __future__ import annotations

from dataclasses import dataclass, field

from utils import get_input_path


@dataclass
class Directory:
    name: str
    size: int = 0
    children: dict[str, Directory] = field(default_factory=dict)
    parent: Directory | None = None
    recursive_visited: bool = False


with open(get_input_path(7)) as f:
    output = f.read().splitlines()


root = Directory("/")
cur_dir: Directory = root
for line in output:
    if line.startswith("$ cd"):
        next_dir = line.split()[-1]
        if next_dir == "/":
            cur_dir = root
        elif next_dir == ".." and cur_dir.parent:
            cur_dir = cur_dir.parent
        else:
            cur_dir = cur_dir.children[next_dir]
    elif line.startswith("dir"):
        dir_name = line.split()[-1]
        cur_dir.children[dir_name] = Directory(dir_name, parent=cur_dir)
    elif line[0].isdigit():
        cur_dir.size += int(line.split()[0])

stack = [root]
while stack:
    cur_dir = stack[-1]
    if not cur_dir.children or cur_dir.recursive_visited:
        stack.pop()
        if cur_dir.parent:
            cur_dir.parent.size += cur_dir.size
    elif not cur_dir.recursive_visited:
        stack.extend(cur_dir.children.values())
        cur_dir.recursive_visited = True

total_size_small_dirs = 0
stack = [root]
while stack:
    cur_dir = stack.pop()
    if cur_dir.size <= 100000:
        total_size_small_dirs += cur_dir.size
    stack.extend(cur_dir.children.values())
assert total_size_small_dirs == 1743217
