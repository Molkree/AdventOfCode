#include "days.h"

#include <iostream>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <cctype>
#include <queue>

using namespace std;

unordered_map<string, set<string>> build_rules(vector<string> rule_lines)
{
    unordered_map<string, set<string>> bottom_up;
    for (auto& rule : rule_lines)
    {
        auto key_values = split_string(rule, "s contain ");
        auto& key = key_values[0];
        auto& values_string = key_values[1];
        values_string.pop_back(); // period
        auto values = split_string(values_string, ", ");
        transform(values.begin(), values.end(), values.begin(), [](string value)
        {
            if (isdigit(static_cast<unsigned char>(value[0])))
            {
                if (value[0] == '1')
                {
                    return value;
                }
                else
                {
                    value.pop_back();
                    return value;
                }
            }
            else
            {
                return string();
            }
        });
        if (values[0].empty())
        {
            values.clear();
        }
        vector<string> bag_names(values);
        transform(bag_names.begin(), bag_names.end(), bag_names.begin(), [](string bag_name)
        {
            return bag_name.substr(2);
        });
        for (auto& bag_name : bag_names)
        {
            bottom_up[bag_name].insert(key);

        }
    }
    return bottom_up;
}

void Day07()
{
    cout << "Day 07" << endl;
    auto rule_lines = read_lines("../input/input07.txt");
    auto bottom_up = build_rules(rule_lines);
    set<string> part1(bottom_up["shiny gold bag"]);
    queue<string> queue;
    const auto queue_push_range = [](std::queue<string>& queue, set<string> set)
    {
        for_each(set.begin(), set.end(), [&](string bag_name)
        {
            queue.emplace(bag_name);
        });
    };
    queue_push_range(queue, part1);
    while (!queue.empty())
    {
        auto& bag = queue.front();
        if (!bottom_up.contains(bag))
        {
            queue.pop();
            continue;
        }
        set<string> new_result(part1);
        new_result.merge(bottom_up[bag]);
        queue.pop();
        set<string> difference;
        set_difference(new_result.begin(), new_result.end(), part1.begin(), part1.end(), inserter(difference, difference.end()));
        queue_push_range(queue, difference);
        part1 = new_result;
    }

    cout << "Part 1: " << part1.size() << endl;
    cout << "Part 2: " << endl;

    cout << endl;
}
