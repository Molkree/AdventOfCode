#include "days.h"

#include <iostream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

unordered_map<string, unordered_set<string>> build_rules(vector<string> rule_lines)
{
    unordered_map<string, unordered_set<string>> bottom_up;
    string delimiter = "s contain ";
    for (auto& rule : rule_lines)
    {
        auto key_values = split_string(rule, delimiter);
        auto& key = key_values[0];
        auto& values = key_values[1];
        values.pop_back(); // period
    }
    return bottom_up;
}

void Day07()
{
    cout << "Day 07" << endl;
    auto rule_lines = read_lines("../input/input07.txt");
    auto bottom_up = build_rules(rule_lines);

    cout << "Part 1: " << endl;
    cout << "Part 2: " << endl;

    cout << endl;
}
