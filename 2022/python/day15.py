import re

from utils import get_input_path

TARGET_ROW = 2000000


def add_interval(
    intervals: list[tuple[int, int]], start: int, end: int
) -> list[tuple[int, int]]:
    """Add interval to list of intervals, merging overlapping intervals."""
    intervals.append((start, end))
    intervals.sort()
    merged_intervals: list[tuple[int, int]] = []
    for interval in intervals:
        if not merged_intervals or merged_intervals[-1][1] < interval[0]:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1] = (
                merged_intervals[-1][0],
                max(merged_intervals[-1][1], interval[1]),
            )
            if len(merged_intervals) > 1 and (
                merged_intervals[-2][1] + 1 == merged_intervals[-1][0]
            ):
                merged_intervals[-2] = (
                    merged_intervals[-2][0],
                    merged_intervals[-1][1],
                )
                merged_intervals.pop()
    return merged_intervals


def remove_point(intervals: list[tuple[int, int]], x: int) -> list[tuple[int, int]]:
    """Remove point from list of intervals, splitting intervals if necessary."""
    for i, (start, end) in enumerate(intervals):
        if start <= x <= end:
            if start == end:
                del intervals[i]
            elif start == x:
                intervals[i] = (start + 1, end)
            elif end == x:
                intervals[i] = (start, end - 1)
            else:
                intervals[i] = (start, x - 1)
                intervals.insert(i + 1, (x + 1, end))
            break
    return intervals


beacons: list[tuple[int, int]] = []
intervals: list[tuple[int, int]] = []
with open(get_input_path(15)) as f:
    for line in f:
        match = re.search(
            "Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line
        )
        if match:
            sensor_x, sensor_y, beacon_x, beacon_y = map(int, match.groups())
            radius = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            distance = abs(TARGET_ROW - sensor_y)
            if distance > radius:
                continue
            beacons.append((beacon_x, beacon_y))
            if beacon_y == TARGET_ROW:
                intervals = add_interval(intervals, beacon_x, beacon_x)
            margin = radius - distance
            intervals = add_interval(intervals, sensor_x - margin, sensor_x + margin)
for beacon_x, beacon_y in beacons:
    if beacon_y == TARGET_ROW:
        intervals = remove_point(intervals, beacon_x)
scanned_length = sum(end - start + 1 for start, end in intervals)
assert scanned_length == 5335787
