#include "days.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <iterator>

using namespace std;

inline vector<int> read_numbers(const string & file_name)
{
    ifstream infile(file_name);
    const istream_iterator<int> start(infile), end;
    vector<int> numbers(start, end);

    return numbers;
}

void Day01()
{
    cout << "Day 01" << endl;
    auto numbers = read_numbers("../input/input01.txt");
    for (size_t i = 0; i < numbers.size(); ++i)
    {
        for (size_t j = i + 1; j < numbers.size(); ++j)
        {
            if (numbers[i] + numbers[j] == 2020)
            {
                cout << "Part 1: " << numbers[i] * numbers[j] << endl;
            }
            for (size_t k = j + 1; k < numbers.size(); ++k)
            {
                if (numbers[i] + numbers[j] + numbers[k] == 2020)
                {
                    cout << "Part 2: " << numbers[i] * numbers[j] * numbers[k] << endl;
                }
            }
        }
    }

    cout << endl;
}
