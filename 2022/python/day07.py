from bisect import bisect
from dataclasses import dataclass, field

from utils import get_input_path


@dataclass
class Directory:
    name: str
    size: int = 0
    children: dict[str, Directory] = field(default_factory=dict)
    parent: Directory | None = None
    __hash__ = object.__hash__


with open(get_input_path(7)) as f:
    output = f.read().splitlines()


root = Directory("/")
cur_dir = root
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
dir_sizes: dict[Directory, int] = {}
while stack:
    cur_dir = stack[-1]
    if cur_dir in dir_sizes:
        stack.pop()
        dir_sizes[cur_dir] = cur_dir.size
        if cur_dir.parent:
            cur_dir.parent.size += cur_dir.size
    else:
        stack.extend(cur_dir.children.values())
        dir_sizes[cur_dir] = 0

sorted_sizes = sorted(dir_sizes.values())
total_size_small_dirs = sum(sorted_sizes[: bisect(sorted_sizes, 100000)])
assert total_size_small_dirs == 1743217

need_to_delete = 30000000 - (70000000 - root.size)
smallest_size_to_delete = sorted_sizes[bisect(sorted_sizes, need_to_delete)]
assert smallest_size_to_delete == 8319096
