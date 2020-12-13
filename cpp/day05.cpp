#include "days.h"

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int partition(const string& seat_string, int upper_bound, char lower_half_char,
    int iterations, size_t string_start_position = 0) noexcept
{
    int lower_bound = 0;
    for (size_t i = string_start_position; i < string_start_position + iterations; ++i)
    {
        const int middle = lower_bound + (upper_bound - lower_bound) / 2;
        if (seat_string[i] == lower_half_char)
        {
            upper_bound = middle;
        }
        else
        {
            lower_bound = middle + 1;
        }
    }
    return lower_bound;
}

int get_seat_id(const string& seat_string) noexcept
{
    const auto row = partition(seat_string, 127, 'F', 7);
    const auto column = partition(seat_string, 7, 'L', 3, 7);
    return row * 8 + column;
}

void Day05()
{
    auto seats = read_lines("../input/input05.txt");
    vector<int> seat_ids(seats.size());
    transform(seats.begin(), seats.end(), seat_ids.begin(), get_seat_id);
    sort(seat_ids.begin(), seat_ids.end());
    int my_seat = 0;
    for (size_t i = 0; i < seat_ids.size(); ++i)
    {
        if (seat_ids[i + 1] != seat_ids[i] + 1)
        {
            my_seat = seat_ids[i] + 1;
            break;
        }
    }

    cout << "Part 1: " << seat_ids[seat_ids.size() - 1] << endl;
    cout << "Part 2: " << my_seat << endl;

    cout << endl;
}
