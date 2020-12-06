using System;
using System.IO;
using System.Text.RegularExpressions;

namespace AdventOfCode2020
{
    public class Day03
    {
        public static void Execute()
        {
            var lines = File.ReadAllLines("../../../../input/input03.txt");
            var width = lines[0].Length;
            var height = lines.Length;
            ulong Slide(int dy, int dx)
            {
                int x = 0, y = 0;
                var treesEncountered = 0ul;
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
            }

            Console.WriteLine($"Part 1: {Slide(1, 3)}");
            Console.WriteLine($"Part 2: {Slide(1, 1) * Slide(1, 3) * Slide(1, 5) * Slide(1, 7) * Slide (2, 1)}");
            Console.WriteLine();
        }
    }
}
