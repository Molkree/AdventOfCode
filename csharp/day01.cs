using System;
using System.IO;
using System.Linq;

namespace AdventOfCode2020
{
    public class Day01
    {
        public static void Execute()
        {
            var numbers = File.ReadAllLines("../input/input01.txt").Select(x => int.Parse(x)).ToArray();
            for (var i = 0; i < numbers.Length; i++)
            {
                for (var j = i + 1; j < numbers.Length; j++)
                {
                    if (numbers[i] + numbers[j] == 2020)
                    {
                        Console.WriteLine("Part 1: {0}", numbers[i] * numbers[j]);
                    }
                    for (var k = j + 1; k < numbers.Length; k++)
                    {
                        if (numbers[i] + numbers[j] + numbers[k] == 2020)
                        {
                            Console.WriteLine("Part 2: {0}", numbers[i] * numbers[j] * numbers[k]);
                        }
                    }
                }
            }
            Console.WriteLine();
        }
    }
}
