#include "days.h"

#include <iostream>
#include <vector>
#include <string>

using namespace std;

void Day03()
{
    cout << "Day 03" << endl;
    auto lines = read_lines("../input/input03.txt");

    const auto width = lines[0].length();
    const auto height = lines.size();
    const auto slide = [&](int dy, int dx)
    {
        auto x = 0ull, y = 0ull, treesEncountered = 0ull;
        while (y < height - dy)
        {
            y += dy;
            x = (x + dx) % width;
            if (lines[y][x] == '#')
            {
                ++treesEncountered;
            }
        }
        return treesEncountered;
    };
    const auto slide1 = slide(1, 1);
    const auto slide2 = slide(1, 3);
    const auto slide3 = slide(1, 5);
    const auto slide4 = slide(1, 7);
    const auto slide5 = slide(2, 1);

    cout << "Part 1: " << slide2 << endl;
    cout << "Part 2: " << slide1 * slide2 * slide3 * slide4 * slide5 << endl;

    cout << endl;
}
