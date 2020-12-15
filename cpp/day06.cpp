#include "days.h"

#include <iostream>
#include <algorithm>
#include <numeric>
#include <iterator>

using namespace std;

void Day06()
{
    cout << "Day 06" << endl;
    auto groups = read_line_groups("../input/input06.txt");
    vector<size_t> part1_group_counts(groups.size());
    transform(groups.begin(), groups.end(), part1_group_counts.begin(), [](string group)
    {
        group.erase(remove(group.begin(), group.end(), '\n'), group.end());
        sort(group.begin(), group.end());
        group.erase(unique(group.begin(), group.end()), group.end());
        return group.size();
    });
    auto part1 = accumulate(part1_group_counts.begin(), part1_group_counts.end(), 0ull);

    vector<size_t> part2_group_counts(groups.size());
    transform(groups.begin(), groups.end(), part2_group_counts.begin(), [](string group)
    {
        auto split_group = split_lines(group);
        auto intersection = accumulate(split_group.begin(), split_group.end(), split_group[0], [](string x, string y)
        {
            sort(x.begin(), x.end());
            sort(y.begin(), y.end());
            string intersection;
            set_intersection(x.begin(), x.end(), y.begin(), y.end(), back_inserter(intersection));
            return intersection;
        });
        return intersection.size();
    });
    auto part2 = accumulate(part2_group_counts.begin(), part2_group_counts.end(), 0ull);

    cout << "Part 1: " << part1 << endl;
    cout << "Part 2: " << part2 << endl;

    cout << endl;
}
