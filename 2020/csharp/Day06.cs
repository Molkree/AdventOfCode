using System;
using System.IO;
using System.Linq;

namespace AdventOfCode2020
{
    public class Day06
    {
        public static void Execute()
        {
            Console.WriteLine("Day 06");
            var file = File.ReadAllText("../input/input06.txt");
            var groups = file.Split("\n\n");
            groups[^1] = string.Concat(groups[^1].SkipLast(1)); // skip last \n
            var part1 = groups
                .Select(group => group.Replace("\n", ""))
                .Select(group => group.Distinct())
                .Select(group => group.Count())
                .Sum();
            var part2 = groups
                .Select(group => group.Split('\n'))
                .Select(group => group.Aggregate((x, y) => string.Concat(x.Intersect(y))))
                .Select(group => group.Length)
                .Sum();

            Console.WriteLine($"Part 1: {part1}");
            Console.WriteLine($"Part 2: {part2}");
            Console.WriteLine();
        }
    }
}
