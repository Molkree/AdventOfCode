#include "days.h"

#include <iostream>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <cctype>
#include <queue>
#include <utility>

using namespace std;

struct Bag
{
    string Name;
    int Required_number = 0;
    Bag(string bag_string) :
        Name(bag_string.substr(2)),
        Required_number(bag_string[0] - '0')
    {
    }

    const bool operator<(const Bag& other) const noexcept
    {
        return Name < other.Name;
    }

    Bag() noexcept
    {
    }
};

void trim_bag_strings(vector<string>& bag_strings)
{
    transform(bag_strings.begin(), bag_strings.end(), bag_strings.begin(), [](string value) noexcept
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
}

pair<unordered_map<string, set<string>>, unordered_map<string, set<Bag>>> build_rules(vector<string> rule_lines)
{
    unordered_map<string, set<string>> bottom_up;
    unordered_map<string, set<Bag>> top_down;
    for (const auto& rule : rule_lines)
    {
        auto key_values = split_string(rule, "s contain ");
        const auto& key = key_values[0];
        auto& bags_string = key_values[1];
        bags_string.pop_back(); // period
        auto bag_strings = split_string(bags_string, ", ");
        trim_bag_strings(bag_strings);
        if (bag_strings[0].empty())
        {
            bag_strings.clear();
        }
        vector<string> bag_names(bag_strings);
        transform(bag_names.begin(), bag_names.end(), bag_names.begin(), [](string bag_name)
        {
            return bag_name.substr(2);
        });
        for (const auto& bag_name : bag_names)
        {
            bottom_up[bag_name].emplace(key);
        }
        vector<Bag> bags(bag_strings.size());
        for_each(bag_strings.begin(), bag_strings.end(), [&](string bag_string)
        {
            top_down[key].emplace(Bag(bag_string));
        });
    }
    return { bottom_up, top_down };
}

int DFS(const unordered_map<string, set<Bag>>& rules, const string& bag)
{
    int sum = 0;
    if (rules.contains(bag))
    {
        for (const auto& inner_bag : rules.at(bag))
        {
            sum += (1 + DFS(rules, inner_bag.Name)) * inner_bag.Required_number;
        }
    }
    return sum;
}

void Day07()
{
    cout << "Day 07" << endl;
    const auto& rule_lines = read_lines("../input/input07.txt");
    auto [bottom_up, top_down] = build_rules(rule_lines);
    set<string> part1(bottom_up["shiny gold bag"]);
    queue<string> queue;
    const auto& queue_push_range = [](std::queue<string>& queue, set<string> set)
    {
        for_each(set.begin(), set.end(), [&](string bag_name)
        {
            queue.emplace(bag_name);
        });
    };
    queue_push_range(queue, part1);
    while (!queue.empty())
    {
        const auto& bag = queue.front();
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
    cout << "Part 2: " << DFS(top_down, "shiny gold bag") << endl;

    cout << endl;
}
