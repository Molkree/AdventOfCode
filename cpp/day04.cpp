#include "days.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <streambuf>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <unordered_map>
#include <regex>
#include <unordered_set>

using namespace std;

inline vector<string> read_line_groups(const string& file_name)
{
    ifstream infile(file_name);
    string str((istreambuf_iterator<char>(infile)),
        istreambuf_iterator<char>());
    vector<string> result;
    string delimiter = "\n\n";

    size_t pos = 0;
    string token;
    while ((pos = str.find(delimiter)) != string::npos)
    {
        token = str.substr(0, pos);
        result.push_back(token);
        str.erase(0, pos + delimiter.length());
    }
    result.push_back(str.substr(0, str.length() - 1)); // last group without \n at the end

    return result;
}

bool int_try_parse(const string& maybe_int, int & out_int)
{
    try
    {
        out_int = stoi(maybe_int);
        return true;
    }
    catch (...)
    {
        return false;
    }
}

bool check_year(const unordered_map<string, string>& key_value_pairs, const string & field, int lower_bound, int upper_bound)
{
    if (const auto iter = key_value_pairs.find(field); iter != key_value_pairs.end())
    {
        int year;
        if (int_try_parse(iter->second, year) && lower_bound <= year && year <= upper_bound)
        {
            return true;
        }
    }
    return false;
}

bool check_height(const unordered_map<string, string>& dict)
{
    if (const auto iter = dict.find("hgt"); iter != dict.end())
    {
        auto& height_string = iter->second;
        const auto check_height_string = [](const string& height_string, const string& suffix, int lower_bound, int upper_bound)
        {
            auto height = 0;
            const size_t string_length = height_string.size();
            return height_string.substr(string_length - suffix.size()) == suffix &&
                int_try_parse(height_string.substr(0, string_length - suffix.size()), height) &&
                lower_bound <= height && height <= upper_bound;
        };
        if (check_height_string(height_string, "cm", 150, 193) ||
            check_height_string(height_string, "in", 59, 76))
        {
            return true;
        }
    }
    return false;
}

bool check_hair_color(const unordered_map<string, string>& dict)
{
    if (const auto iter = dict.find("hcl"); iter != dict.end())
    {
        auto& hair_string = iter->second;
        if (hair_string[0] == '#' && hair_string.size() == 7 &&
            regex_match(hair_string.substr(1), regex("[0-9a-z]+")))
        {
            return true;
        }
    }
    return false;
}

bool check_eye_color(const unordered_map<string, string>& dict)
{
    if (const auto iter = dict.find("ecl"); iter != dict.end())
    {
        unordered_set<string> eye_colors({ "amb", "blu", "brn", "gry", "grn", "hzl", "oth" });
        if (eye_colors.contains(iter->second))
        {
            return true;
        }
    }
    return false;
}

bool check_passport_id(const unordered_map<string, string>& dict)
{
    if (const auto iter = dict.find("pid"); iter != dict.end())
    {
        auto& pid = iter->second;
        if (pid.size() == 9 && regex_match(pid, regex("[0-9]+")))
        {
            return true;
        }
    }
    return false;
}

bool is_valid_passport(string fields)
{
    replace(fields.begin(), fields.end(), ' ', '\n');
    vector<string> separated_fields;
    istringstream iss(fields);
    copy(istream_iterator<string>(iss),
        istream_iterator<string>(),
        back_inserter(separated_fields));
    unordered_map<string, string> dict;
    for (const auto& field : separated_fields)
    {
        const auto pos = field.find(':');
        dict[field.substr(0, pos)] = field.substr(pos + 1, field.size() - pos - 1);
    }

    if (check_year(dict, "byr", 1920, 2002) &&
        check_year(dict, "iyr", 2010, 2020) &&
        check_year(dict, "eyr", 2020, 2030) &&
        check_height(dict) &&
        check_hair_color(dict) &&
        check_eye_color(dict) &&
        check_passport_id(dict))
    {
        return true;
    }

    return false;
}

void Day04()
{
    cout << "Day 04" << endl;
    auto passwords = read_line_groups("../input/input04.txt");

    const auto valid_passports_count_1 = count_if(passwords.begin(), passwords.end(), [](const auto& password) noexcept
    {
        return
            password.find("byr") != string::npos &&
            password.find("iyr") != string::npos &&
            password.find("eyr") != string::npos &&
            password.find("hgt") != string::npos &&
            password.find("hcl") != string::npos &&
            password.find("ecl") != string::npos &&
            password.find("pid") != string::npos;
    });
    cout << "Part 1: " << valid_passports_count_1 << endl;

    is_valid_passport(passwords[3]);
    const auto valid_passports_count_2 = count_if(passwords.begin(), passwords.end(), is_valid_passport);
    cout << "Part 2: " << valid_passports_count_2 << endl;

    cout << endl;
}
