#ifndef DAYS
#define DAYS

#include <vector>
#include <string>

std::vector<std::string> read_lines(const std::string& file_name);
std::vector<std::string> split_string(const std::string& str, char delimiter = '\n');
std::vector<std::string> split_string(const std::string& str, const std::string& delimiter = "\n");
std::vector<std::string> read_line_groups(const std::string& file_name);

void Day01();
void Day02();
void Day03();
void Day04();
void Day05();
void Day06();
void Day07();

#endif
