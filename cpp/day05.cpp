#include "days.h"

#include <iostream>
#include <string>

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
    int max_seat_id = 0;
    for (const auto& seat : seats)
    {
        const auto seat_id = get_seat_id(seat);
        if (max_seat_id < seat_id)
        {
            max_seat_id = seat_id;
        }
    }

    cout << "Part 1: " << max_seat_id << endl;
    cout << "Part 2: " << endl;

    cout << endl;
}
